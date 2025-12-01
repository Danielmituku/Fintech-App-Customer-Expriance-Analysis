"""
Main runner script for Task 1: Data Collection and Preprocessing
This script orchestrates the scraping and preprocessing pipeline
"""

import os
import sys

# Add scripts directory to path
scripts_dir = os.path.dirname(__file__)
sys.path.append(scripts_dir)

from scraping.scrape_reviews import main as scrape_main
from preprocessing.preprocess_reviews import main as preprocess_main


def main():
    """
    Run the complete Task 1 pipeline
    """
    print("=" * 70)
    print("TASK 1: Data Collection and Preprocessing")
    print("=" * 70)
    
    # Step 1: Scrape reviews
    print("\n" + "=" * 70)
    print("STEP 1: Scraping Reviews from Google Play Store")
    print("=" * 70)
    try:
        scrape_main()
    except Exception as e:
        print(f"\n✗ Error during scraping: {str(e)}")
        print("Please check:")
        print("  1. App IDs are correct in scrape_reviews.py")
        print("  2. Internet connection is working")
        print("  3. google-play-scraper is installed (pip install google-play-scraper)")
        return
    
    # Step 2: Preprocess data
    print("\n" + "=" * 70)
    print("STEP 2: Preprocessing and Cleaning Data")
    print("=" * 70)
    try:
        preprocess_main()
    except Exception as e:
        print(f"\n✗ Error during preprocessing: {str(e)}")
        return
    
    print("\n" + "=" * 70)
    print("✓ TASK 1 COMPLETED SUCCESSFULLY")
    print("=" * 70)
    print("\nNext steps:")
    print("  1. Review the cleaned data in data/processed/cleaned_reviews.csv")
    print("  2. Verify data quality meets requirements (<5% missing data)")
    print("  3. Commit changes to task-1 branch")
    print("  4. Proceed to Task 2: Sentiment and Thematic Analysis")


if __name__ == "__main__":
    main()

