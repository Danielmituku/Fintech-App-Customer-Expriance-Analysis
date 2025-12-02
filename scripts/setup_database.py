#!/usr/bin/env python3
"""
Setup script for Task 3: Create PostgreSQL database and schema
Run this script first before loading data
"""

import logging
import sys
from pathlib import Path

try:
    import psycopg2
    from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
except ImportError:
    print("ERROR: psycopg2 not installed. Install via: pip install psycopg2-binary")
    sys.exit(1)

sys.path.insert(0, str(Path(__file__).parent.parent))
from src.fintech_app_reviews.config import load_config

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)


def create_database():
    """Create the bank_reviews database if it doesn't exist"""
    try:
        config = load_config("configs/db.yaml")
        db_config = config.get("postgres", {})
        
        # Connect to default postgres database to create our database
        conn = psycopg2.connect(
            host=db_config.get("host", "localhost"),
            port=db_config.get("port", 5432),
            database="postgres",  # Connect to default database
            user=db_config.get("user", "postgres"),
            password=db_config.get("password", "postgres")
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        
        db_name = db_config.get("database", "bank_reviews")
        
        with conn.cursor() as cur:
            # Check if database exists
            cur.execute(
                "SELECT 1 FROM pg_database WHERE datname = %s",
                (db_name,)
            )
            exists = cur.fetchone()
            
            if not exists:
                cur.execute(f'CREATE DATABASE "{db_name}"')
                logger.info(f"✓ Database '{db_name}' created successfully")
            else:
                logger.info(f"✓ Database '{db_name}' already exists")
        
        conn.close()
        return True
        
    except Exception as e:
        logger.error(f"Failed to create database: {e}")
        logger.info("\nTroubleshooting:")
        logger.info("1. Make sure PostgreSQL is installed and running")
        logger.info("2. Check your credentials in configs/db.yaml")
        logger.info("3. Try: psql -U postgres -c 'CREATE DATABASE bank_reviews;'")
        return False


def main():
    """Main setup function"""
    logger.info("=" * 70)
    logger.info("Task 3: PostgreSQL Database Setup")
    logger.info("=" * 70)
    
    logger.info("\nStep 1: Creating database 'bank_reviews'...")
    if create_database():
        logger.info("\n✓ Database setup complete!")
        logger.info("\nNext steps:")
        logger.info("1. Update configs/db.yaml with your PostgreSQL password if needed")
        logger.info("2. Run: python scripts/load_to_postgres.py")
    else:
        logger.error("\n✗ Database setup failed. Please fix the issues above.")


if __name__ == "__main__":
    main()

