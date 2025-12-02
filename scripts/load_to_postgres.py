#!/usr/bin/env python3
"""
Task 3: Load cleaned and processed review data into PostgreSQL database
"""

import logging
import os
import pandas as pd
from pathlib import Path

try:
    import psycopg2
    from psycopg2.extras import execute_values
except ImportError:
    logging.error("psycopg2 not installed. Install via: pip install psycopg2-binary")
    raise

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.fintech_app_reviews.config import load_config

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)


def get_db_connection():
    """Get PostgreSQL database connection from config"""
    try:
        config = load_config("configs/db.yaml")
        db_config = config.get("postgres", {})
        
        conn = psycopg2.connect(
            host=db_config.get("host", "localhost"),
            port=db_config.get("port", 5432),
            database=db_config.get("database", "bank_reviews"),
            user=db_config.get("user", "postgres"),
            password=db_config.get("password", "postgres")
        )
        logger.info("Connected to PostgreSQL database")
        return conn
    except Exception as e:
        logger.error(f"Failed to connect to database: {e}")
        logger.info("Make sure PostgreSQL is running and database exists")
        logger.info("Update configs/db.yaml with your database credentials")
        raise


def create_schema(conn):
    """Create database schema if it doesn't exist"""
    try:
        with conn.cursor() as cur:
            # Read schema file
            schema_file = Path("src/fintech_app_reviews/db/schema.sql")
            if schema_file.exists():
                with open(schema_file, 'r') as f:
                    schema_sql = f.read()
                cur.execute(schema_sql)
                conn.commit()
                logger.info("Database schema created/verified")
            else:
                # Create schema inline if file doesn't exist
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS banks (
                        bank_id SERIAL PRIMARY KEY,
                        bank_name VARCHAR(255) NOT NULL UNIQUE,
                        app_name VARCHAR(255)
                    );
                """)
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS reviews (
                        review_id VARCHAR(255) PRIMARY KEY,
                        bank_id INTEGER REFERENCES banks(bank_id),
                        review_text TEXT,
                        rating INTEGER,
                        review_date DATE,
                        sentiment_label VARCHAR(50),
                        sentiment_score FLOAT,
                        source VARCHAR(100),
                        themes TEXT,
                        keywords TEXT
                    );
                """)
                conn.commit()
                logger.info("Database schema created")
    except Exception as e:
        logger.error(f"Failed to create schema: {e}")
        conn.rollback()
        raise


def get_or_create_bank_id(conn, bank_name, app_name=None):
    """Get bank_id if exists, otherwise create and return new bank_id"""
    with conn.cursor() as cur:
        # Try to get existing bank_id
        cur.execute("SELECT bank_id FROM banks WHERE bank_name = %s", (bank_name,))
        result = cur.fetchone()
        if result:
            return result[0]
        
        # Create new bank
        cur.execute(
            "INSERT INTO banks (bank_name, app_name) VALUES (%s, %s) RETURNING bank_id",
            (bank_name, app_name or bank_name)
        )
        bank_id = cur.fetchone()[0]
        conn.commit()
        logger.info(f"Created new bank entry: {bank_name} (ID: {bank_id})")
        return bank_id


def load_data_to_db(conn, df):
    """Load DataFrame into PostgreSQL database"""
    try:
        # Ensure required columns exist
        required_cols = ['review', 'rating', 'date', 'bank', 'source']
        col_mapping = {
            'review': 'review_text',
            'date': 'review_date'
        }
        
        # Map column names
        df_mapped = df.copy()
        for old_col, new_col in col_mapping.items():
            if old_col in df_mapped.columns:
                df_mapped[new_col] = df_mapped[old_col]
        
        # Get or create bank IDs
        bank_ids = {}
        for bank_name in df_mapped['bank'].unique():
            bank_ids[bank_name] = get_or_create_bank_id(conn, bank_name)
        
        # Prepare data for insertion
        records = []
        for _, row in df_mapped.iterrows():
            bank_name = row.get('bank', 'Unknown')
            bank_id = bank_ids.get(bank_name)
            
            # Generate review_id if not present
            review_id = row.get('review_id') or row.get('reviewId') or f"{bank_id}_{hash(str(row.get('review_text', '')))}"
            
            record = (
                str(review_id),
                bank_id,
                str(row.get('review_text', row.get('review', ''))),
                int(row.get('rating', 0)) if pd.notna(row.get('rating')) else None,
                pd.to_datetime(row.get('review_date', row.get('date')), errors='coerce').date() if pd.notna(row.get('review_date', row.get('date'))) else None,
                row.get('sentiment_label', ''),
                float(row.get('sentiment_score', 0)) if pd.notna(row.get('sentiment_score')) else None,
                row.get('source', 'Google Play Store'),
                row.get('themes', ''),
                row.get('keywords', '')
            )
            records.append(record)
        
        # Batch insert
        with conn.cursor() as cur:
            execute_values(
                cur,
                """INSERT INTO reviews 
                   (review_id, bank_id, review_text, rating, review_date, 
                    sentiment_label, sentiment_score, source, themes, keywords)
                   VALUES %s
                   ON CONFLICT (review_id) DO UPDATE SET
                   sentiment_label = EXCLUDED.sentiment_label,
                   sentiment_score = EXCLUDED.sentiment_score,
                   themes = EXCLUDED.themes,
                   keywords = EXCLUDED.keywords
                """,
                records
            )
            conn.commit()
            logger.info(f"Inserted/updated {len(records)} reviews")
        
        return len(records)
    except Exception as e:
        logger.error(f"Failed to load data: {e}")
        conn.rollback()
        raise


def verify_data_integrity(conn):
    """Run SQL queries to verify data integrity"""
    logger.info("\nVerifying data integrity...")
    try:
        with conn.cursor() as cur:
            # Count reviews per bank
            cur.execute("""
                SELECT b.bank_name, COUNT(r.review_id) as review_count, 
                       AVG(r.rating) as avg_rating
                FROM banks b
                LEFT JOIN reviews r ON b.bank_id = r.bank_id
                GROUP BY b.bank_id, b.bank_name
                ORDER BY review_count DESC;
            """)
            results = cur.fetchall()
            logger.info("\nReviews per bank:")
            for bank_name, count, avg_rating in results:
                logger.info(f"  {bank_name}: {count} reviews, avg rating: {avg_rating:.2f}")
            
            # Total review count
            cur.execute("SELECT COUNT(*) FROM reviews;")
            total = cur.fetchone()[0]
            logger.info(f"\nTotal reviews in database: {total}")
            
            # Sentiment distribution
            cur.execute("""
                SELECT sentiment_label, COUNT(*) as count
                FROM reviews
                WHERE sentiment_label IS NOT NULL AND sentiment_label != ''
                GROUP BY sentiment_label;
            """)
            sentiment_results = cur.fetchall()
            logger.info("\nSentiment distribution:")
            for label, count in sentiment_results:
                logger.info(f"  {label}: {count}")
            
            return True
    except Exception as e:
        logger.error(f"Data integrity check failed: {e}")
        return False


def main():
    """Main function to load data into PostgreSQL"""
    logger.info("=" * 70)
    logger.info("TASK 3: Load Data to PostgreSQL")
    logger.info("=" * 70)
    
    # Find input file
    input_files = [
        "data/processed/reviews_with_themes.csv",
        "data/processed/reviews_with_sentiment.csv",
        "data/processed/reviews.csv",
        "data/interim/interim_reviews.csv"
    ]
    
    input_file = None
    for file in input_files:
        if os.path.exists(file):
            input_file = file
            break
    
    if not input_file:
        logger.error("No input data file found. Please run Task 2 first.")
        return
    
    logger.info(f"Loading data from: {input_file}")
    
    try:
        # Load data
        df = pd.read_csv(input_file)
        logger.info(f"Loaded {len(df)} reviews")
        
        # Connect to database
        conn = get_db_connection()
        
        # Create schema
        create_schema(conn)
        
        # Load data
        load_data_to_db(conn, df)
        
        # Verify integrity
        verify_data_integrity(conn)
        
        conn.close()
        logger.info("\n✓ TASK 3 COMPLETED SUCCESSFULLY")
        
    except Exception as e:
        logger.error(f"✗ Task 3 failed: {e}")
        raise


if __name__ == "__main__":
    main()

