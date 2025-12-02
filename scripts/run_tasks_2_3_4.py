#!/usr/bin/env python3
"""
Master script to run Tasks 2, 3, and 4:
- Task 2: Sentiment and Thematic Analysis
- Task 3: PostgreSQL Database Storage
- Task 4: Insights and Recommendations
"""

import logging
import os
import sys
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - [MASTER] - %(message)s"
)
logger = logging.getLogger("MASTER")

def check_data_exists():
    """Check if processed data exists, if not check for raw data"""
    processed_path = Path("data/processed/reviews.csv")
    interim_path = Path("data/interim/interim_reviews.csv")
    raw_path = Path("data/raw/raw_reviews.csv")
    
    if processed_path.exists():
        logger.info(f"Found processed data: {processed_path}")
        return str(processed_path)
    elif interim_path.exists():
        logger.info(f"Found interim data: {interim_path}")
        return str(interim_path)
    elif raw_path.exists():
        logger.info(f"Found raw data: {raw_path}")
        return str(raw_path)
    else:
        logger.warning("No data files found. Need to collect data first.")
        return None

def run_task2():
    """Run Task 2: Sentiment and Thematic Analysis"""
    logger.info("=" * 70)
    logger.info("TASK 2: Sentiment and Thematic Analysis")
    logger.info("=" * 70)
    
    # Check for input data
    input_file = check_data_exists()
    if not input_file:
        logger.error("No data found. Please run data collection first.")
        return False
    
    # Step 1: Run sentiment analysis
    logger.info("\nStep 1: Running sentiment analysis...")
    try:
        from scripts.run_analysis import run_sentiment
        # Update input path if needed
        run_sentiment(input_csv=input_file)
        logger.info("✓ Sentiment analysis complete")
    except Exception as e:
        logger.error(f"✗ Sentiment analysis failed: {e}")
        return False
    
    # Step 2: Run thematic analysis
    logger.info("\nStep 2: Running thematic analysis...")
    try:
        from scripts.run_theme_extraction import run_theme_extraction
        run_theme_extraction()
        logger.info("✓ Thematic analysis complete")
    except Exception as e:
        logger.error(f"✗ Thematic analysis failed: {e}")
        return False
    
    logger.info("\n✓ TASK 2 COMPLETED")
    return True

def run_task3():
    """Run Task 3: PostgreSQL Database Storage"""
    logger.info("\n" + "=" * 70)
    logger.info("TASK 3: PostgreSQL Database Storage")
    logger.info("=" * 70)
    
    # Check if data with sentiment/themes exists
    input_file = Path("data/processed/reviews_with_themes.csv")
    if not input_file.exists():
        logger.error("No processed data with themes found. Run Task 2 first.")
        return False
    
    logger.info("\nStep 1: Loading data to PostgreSQL...")
    try:
        from scripts.load_to_postgres import main as load_main
        load_main()
        logger.info("✓ Data loaded to PostgreSQL")
    except Exception as e:
        logger.error(f"✗ Database loading failed: {e}")
        logger.info("Note: Make sure PostgreSQL is installed and database is configured")
        return False
    
    logger.info("\n✓ TASK 3 COMPLETED")
    return True

def run_task4():
    """Run Task 4: Insights and Recommendations"""
    logger.info("\n" + "=" * 70)
    logger.info("TASK 4: Insights and Recommendations")
    logger.info("=" * 70)
    
    # Check if data exists
    input_file = Path("data/processed/reviews_with_themes.csv")
    if not input_file.exists():
        logger.error("No processed data found. Run Task 2 first.")
        return False
    
    logger.info("\nStep 1: Generating insights and visualizations...")
    try:
        from scripts.generate_report import main as report_main
        report_main()
        logger.info("✓ Insights and visualizations generated")
    except Exception as e:
        logger.error(f"✗ Report generation failed: {e}")
        return False
    
    logger.info("\n✓ TASK 4 COMPLETED")
    return True

def main():
    """Main orchestrator"""
    logger.info("=" * 70)
    logger.info("Fintech App Review Analysis - Tasks 2, 3, 4 Pipeline")
    logger.info("=" * 70)
    
    # Check if we're in the right directory
    if not Path("scripts").exists():
        logger.error("Please run this script from the project root directory")
        return
    
    # Run tasks sequentially
    task2_success = run_task2()
    
    if task2_success:
        task3_success = run_task3()
        if task3_success:
            run_task4()
        else:
            logger.warning("Task 3 failed, skipping Task 4")
    else:
        logger.error("Task 2 failed, cannot proceed with Tasks 3 and 4")
    
    logger.info("\n" + "=" * 70)
    logger.info("Pipeline execution complete")
    logger.info("=" * 70)

if __name__ == "__main__":
    main()

