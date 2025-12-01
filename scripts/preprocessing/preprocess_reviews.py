"""
Data Preprocessing Script for Bank Reviews
- Removes duplicates
- Handles missing data
- Normalizes dates to YYYY-MM-DD format
- Saves cleaned data as CSV
"""

import pandas as pd
import numpy as np
from datetime import datetime
import os
import sys

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))


def load_raw_data(input_path):
    """
    Load raw scraped data from CSV
    
    Args:
        input_path (str): Path to raw data CSV file
        
    Returns:
        pd.DataFrame: Raw data DataFrame
    """
    try:
        df = pd.read_csv(input_path)
        print(f"✓ Loaded {len(df)} reviews from {input_path}")
        return df
    except FileNotFoundError:
        print(f"✗ Error: File not found at {input_path}")
        return None
    except Exception as e:
        print(f"✗ Error loading data: {str(e)}")
        return None


def remove_duplicates(df):
    """
    Remove duplicate reviews
    
    Args:
        df (pd.DataFrame): Input DataFrame
        
    Returns:
        pd.DataFrame: DataFrame with duplicates removed
    """
    initial_count = len(df)
    
    # Remove duplicates based on review text and bank
    # This handles cases where the same review might appear multiple times
    df_cleaned = df.drop_duplicates(subset=['review', 'bank'], keep='first')
    
    # Also remove duplicates based on review_id if available
    if 'review_id' in df_cleaned.columns:
        df_cleaned = df_cleaned.drop_duplicates(subset=['review_id'], keep='first')
    
    removed_count = initial_count - len(df_cleaned)
    print(f"✓ Removed {removed_count} duplicate reviews ({removed_count/initial_count*100:.2f}%)")
    
    return df_cleaned


def handle_missing_data(df):
    """
    Handle missing data in the DataFrame
    
    Args:
        df (pd.DataFrame): Input DataFrame
        
    Returns:
        pd.DataFrame: DataFrame with handled missing data
    """
    initial_count = len(df)
    
    # Calculate missing data percentage before cleaning
    missing_before = {
        'review': df['review'].isna().sum() + (df['review'] == '').sum(),
        'rating': df['rating'].isna().sum(),
        'date': df['date'].isna().sum(),
        'bank': df['bank'].isna().sum()
    }
    
    print("\nMissing data before cleaning:")
    for col, count in missing_before.items():
        pct = (count / len(df)) * 100
        print(f"  {col}: {count} ({pct:.2f}%)")
    
    # Remove rows where critical fields are missing
    # Keep rows even if some optional fields are missing
    df_cleaned = df.copy()
    
    # Remove rows with missing review text (critical field)
    df_cleaned = df_cleaned[df_cleaned['review'].notna() & (df_cleaned['review'] != '')]
    
    # Remove rows with missing bank name (critical field)
    df_cleaned = df_cleaned[df_cleaned['bank'].notna()]
    
    # For missing ratings, we could fill with median or mode, but for now we'll keep them
    # as NaN since they might be useful for analysis
    
    # Calculate missing data percentage after cleaning
    missing_after = {
        'review': df_cleaned['review'].isna().sum() + (df_cleaned['review'] == '').sum(),
        'rating': df_cleaned['rating'].isna().sum(),
        'date': df_cleaned['date'].isna().sum(),
        'bank': df_cleaned['bank'].isna().sum()
    }
    
    print("\nMissing data after cleaning:")
    for col, count in missing_after.items():
        pct = (count / len(df_cleaned)) * 100 if len(df_cleaned) > 0 else 0
        print(f"  {col}: {count} ({pct:.2f}%)")
    
    removed_count = initial_count - len(df_cleaned)
    if removed_count > 0:
        print(f"\n✓ Removed {removed_count} rows with missing critical data")
    
    # Check if we meet the <5% missing data target
    total_missing = sum(missing_after.values())
    missing_pct = (total_missing / (len(df_cleaned) * len(missing_after))) * 100 if len(df_cleaned) > 0 else 0
    
    if missing_pct < 5:
        print(f"✓ Missing data target met: {missing_pct:.2f}% < 5%")
    else:
        print(f"⚠ Warning: Missing data is {missing_pct:.2f}%, above 5% target")
    
    return df_cleaned


def normalize_dates(df):
    """
    Normalize dates to YYYY-MM-DD format
    
    Args:
        df (pd.DataFrame): Input DataFrame
        
    Returns:
        pd.DataFrame: DataFrame with normalized dates
    """
    df_cleaned = df.copy()
    
    # Convert date column to datetime if it's not already
    if 'date' in df_cleaned.columns:
        # Try to parse the date column
        try:
            # If date is already in a parseable format
            df_cleaned['date'] = pd.to_datetime(df_cleaned['date'], errors='coerce')
            
            # Format to YYYY-MM-DD
            df_cleaned['date'] = df_cleaned['date'].dt.strftime('%Y-%m-%d')
            
            # Count successfully parsed dates
            parsed_count = df_cleaned['date'].notna().sum()
            print(f"✓ Normalized {parsed_count} dates to YYYY-MM-DD format")
            
            # Show date range if available
            valid_dates = df_cleaned[df_cleaned['date'].notna()]['date']
            if len(valid_dates) > 0:
                print(f"  Date range: {valid_dates.min()} to {valid_dates.max()}")
            
        except Exception as e:
            print(f"⚠ Warning: Error normalizing dates: {str(e)}")
    
    return df_cleaned


def select_required_columns(df):
    """
    Select and order required columns for final output
    
    Args:
        df (pd.DataFrame): Input DataFrame
        
    Returns:
        pd.DataFrame: DataFrame with required columns
    """
    required_columns = ['review', 'rating', 'date', 'bank', 'source']
    
    # Check which required columns exist
    available_columns = [col for col in required_columns if col in df.columns]
    missing_columns = [col for col in required_columns if col not in df.columns]
    
    if missing_columns:
        print(f"⚠ Warning: Missing columns: {missing_columns}")
    
    # Select available required columns and keep any additional useful columns
    columns_to_keep = available_columns + [col for col in df.columns if col not in required_columns]
    df_selected = df[columns_to_keep].copy()
    
    # Ensure required columns are in the correct order
    final_columns = [col for col in required_columns if col in df_selected.columns]
    final_columns += [col for col in df_selected.columns if col not in required_columns]
    
    df_selected = df_selected[final_columns]
    
    return df_selected


def save_cleaned_data(df, output_path):
    """
    Save cleaned data to CSV
    
    Args:
        df (pd.DataFrame): Cleaned DataFrame
        output_path (str): Path to save CSV file
    """
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Save to CSV
    df.to_csv(output_path, index=False, encoding='utf-8')
    print(f"\n✓ Cleaned data saved to: {output_path}")
    print(f"Total reviews: {len(df)}")


def main():
    """
    Main preprocessing pipeline
    """
    print("=" * 60)
    print("Data Preprocessing Pipeline")
    print("=" * 60)
    
    # Get the project root directory
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    input_path = os.path.join(project_root, 'data', 'raw', 'raw_reviews.csv')
    output_path = os.path.join(project_root, 'data', 'processed', 'cleaned_reviews.csv')
    
    # Load raw data
    df = load_raw_data(input_path)
    if df is None or df.empty:
        print("✗ No data to process. Please run the scraping script first.")
        return
    
    print(f"\nInitial data shape: {df.shape}")
    
    # Step 1: Remove duplicates
    print("\n" + "-" * 60)
    print("Step 1: Removing duplicates")
    print("-" * 60)
    df = remove_duplicates(df)
    
    # Step 2: Handle missing data
    print("\n" + "-" * 60)
    print("Step 2: Handling missing data")
    print("-" * 60)
    df = handle_missing_data(df)
    
    # Step 3: Normalize dates
    print("\n" + "-" * 60)
    print("Step 3: Normalizing dates")
    print("-" * 60)
    df = normalize_dates(df)
    
    # Step 4: Select required columns
    print("\n" + "-" * 60)
    print("Step 4: Selecting required columns")
    print("-" * 60)
    df = select_required_columns(df)
    
    # Save cleaned data
    print("\n" + "-" * 60)
    print("Saving cleaned data")
    print("-" * 60)
    save_cleaned_data(df, output_path)
    
    # Print final summary
    print("\n" + "=" * 60)
    print("Preprocessing Summary")
    print("=" * 60)
    print(f"Final data shape: {df.shape}")
    print(f"\nReviews per bank:")
    print(df['bank'].value_counts())
    print(f"\nRating distribution:")
    if 'rating' in df.columns:
        print(df['rating'].value_counts().sort_index())
    print(f"\nData quality:")
    print(f"  Missing reviews: {df['review'].isna().sum() + (df['review'] == '').sum()}")
    print(f"  Missing ratings: {df['rating'].isna().sum() if 'rating' in df.columns else 'N/A'}")
    print(f"  Missing dates: {df['date'].isna().sum() if 'date' in df.columns else 'N/A'}")
    print(f"  Missing banks: {df['bank'].isna().sum()}")
    print("=" * 60)


if __name__ == "__main__":
    main()

