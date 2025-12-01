"""
Web Scraping Script for Google Play Store Reviews
Collects reviews, ratings, dates, and app names for three Ethiopian banks
"""

import pandas as pd
from google_play_scraper import app, reviews, Sort
import time
from datetime import datetime
import os
import sys

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# Bank app configurations
# Note: You'll need to find the actual app IDs from Google Play Store
BANK_APPS = {
    'CBE': {
        'app_id': 'com.cbe.mobilebanking',  # Update with actual app ID
        'bank_name': 'Commercial Bank of Ethiopia',
        'app_name': 'CBE Mobile Banking'
    },
    'BOA': {
        'app_id': 'com.bankofabyssinia.mobilebanking',  # Update with actual app ID
        'bank_name': 'Bank of Abyssinia',
        'app_name': 'BOA Mobile Banking'
    },
    'Dashen': {
        'app_id': 'com.dashenbank.mobilebanking',  # Update with actual app ID
        'bank_name': 'Dashen Bank',
        'app_name': 'Dashen Mobile Banking'
    }
}

# Target number of reviews per bank
TARGET_REVIEWS_PER_BANK = 400


def get_app_info(app_id):
    """
    Get basic app information from Google Play Store
    
    Args:
        app_id (str): Google Play Store app ID
        
    Returns:
        dict: App information
    """
    try:
        app_info = app(app_id, lang='en', country='et')  # 'et' for Ethiopia
        return app_info
    except Exception as e:
        print(f"Error fetching app info for {app_id}: {str(e)}")
        return None


def scrape_reviews(app_id, bank_name, app_name, count=400):
    """
    Scrape reviews from Google Play Store
    
    Args:
        app_id (str): Google Play Store app ID
        bank_name (str): Name of the bank
        app_name (str): Name of the app
        count (int): Number of reviews to scrape
        
    Returns:
        list: List of review dictionaries
    """
    all_reviews = []
    continuation_token = None
    reviews_collected = 0
    
    print(f"\nScraping reviews for {bank_name} ({app_name})...")
    print(f"Target: {count} reviews")
    
    try:
        # Get app info first
        app_info = get_app_info(app_id)
        if app_info:
            print(f"App found: {app_info.get('title', 'Unknown')}")
            print(f"Installs: {app_info.get('installs', 'Unknown')}")
            print(f"Rating: {app_info.get('score', 'Unknown')}")
        
        # Scrape reviews in batches
        while reviews_collected < count:
            batch_size = min(200, count - reviews_collected)  # Scrape in batches of 200
            
            try:
                result, continuation_token = reviews(
                    app_id,
                    lang='en',
                    country='et',
                    sort=Sort.NEWEST,  # Sort by newest first
                    count=batch_size,
                    continuation_token=continuation_token
                )
                
                if not result:
                    print(f"No more reviews available. Collected {reviews_collected} reviews.")
                    break
                
                # Process reviews
                for review in result:
                    review_data = {
                        'review': review.get('content', ''),
                        'rating': review.get('score', None),
                        'date': review.get('at', None),
                        'bank': bank_name,
                        'app_name': app_name,
                        'source': 'Google Play Store',
                        'review_id': review.get('reviewId', ''),
                        'thumbs_up': review.get('thumbsUpCount', 0),
                        'reviewer_name': review.get('userName', 'Anonymous')
                    }
                    all_reviews.append(review_data)
                
                reviews_collected = len(all_reviews)
                print(f"Collected {reviews_collected} reviews so far...")
                
                # If we got fewer reviews than requested, we might have reached the end
                if len(result) < batch_size:
                    print(f"Reached end of available reviews. Total collected: {reviews_collected}")
                    break
                
                # Rate limiting - be respectful to Google Play Store
                time.sleep(2)
                
            except Exception as e:
                print(f"Error during review scraping: {str(e)}")
                print(f"Collected {reviews_collected} reviews before error.")
                break
        
        print(f"✓ Successfully collected {len(all_reviews)} reviews for {bank_name}")
        return all_reviews
        
    except Exception as e:
        print(f"✗ Error scraping reviews for {bank_name}: {str(e)}")
        return all_reviews


def scrape_all_banks(target_reviews=400):
    """
    Scrape reviews for all banks
    
    Args:
        target_reviews (int): Target number of reviews per bank
        
    Returns:
        pd.DataFrame: DataFrame containing all reviews
    """
    all_reviews_data = []
    
    for bank_code, bank_info in BANK_APPS.items():
        app_id = bank_info['app_id']
        bank_name = bank_info['bank_name']
        app_name = bank_info['app_name']
        
        reviews_data = scrape_reviews(app_id, bank_name, app_name, target_reviews)
        all_reviews_data.extend(reviews_data)
        
        # Add delay between banks to be respectful
        time.sleep(3)
    
    # Convert to DataFrame
    df = pd.DataFrame(all_reviews_data)
    
    return df


def save_raw_data(df, output_path):
    """
    Save raw scraped data to CSV
    
    Args:
        df (pd.DataFrame): DataFrame with reviews
        output_path (str): Path to save CSV file
    """
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Save to CSV
    df.to_csv(output_path, index=False, encoding='utf-8')
    print(f"\n✓ Raw data saved to: {output_path}")
    print(f"Total reviews collected: {len(df)}")
    print(f"Reviews per bank:")
    print(df['bank'].value_counts())


def main():
    """
    Main function to orchestrate the scraping process
    """
    print("=" * 60)
    print("Google Play Store Review Scraper")
    print("Banks: CBE, BOA, Dashen Bank")
    print("=" * 60)
    
    # Get the project root directory
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    output_path = os.path.join(project_root, 'data', 'raw', 'raw_reviews.csv')
    
    # Scrape reviews
    df = scrape_all_banks(target_reviews=TARGET_REVIEWS_PER_BANK)
    
    if df.empty:
        print("\n✗ No reviews were collected. Please check:")
        print("  1. App IDs are correct")
        print("  2. Internet connection is working")
        print("  3. Apps exist on Google Play Store")
        return
    
    # Save raw data
    save_raw_data(df, output_path)
    
    # Print summary statistics
    print("\n" + "=" * 60)
    print("Scraping Summary")
    print("=" * 60)
    print(f"Total reviews: {len(df)}")
    print(f"\nReviews per bank:")
    print(df['bank'].value_counts())
    print(f"\nRating distribution:")
    print(df['rating'].value_counts().sort_index())
    print(f"\nMissing data:")
    print(f"  Reviews: {df['review'].isna().sum()} ({df['review'].isna().sum()/len(df)*100:.2f}%)")
    print(f"  Ratings: {df['rating'].isna().sum()} ({df['rating'].isna().sum()/len(df)*100:.2f}%)")
    print(f"  Dates: {df['date'].isna().sum()} ({df['date'].isna().sum()/len(df)*100:.2f}%)")
    print("=" * 60)


if __name__ == "__main__":
    main()

