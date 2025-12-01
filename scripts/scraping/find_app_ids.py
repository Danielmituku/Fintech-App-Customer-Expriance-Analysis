"""
Helper script to find Google Play Store app IDs for the banks
This script searches for the apps and displays their app IDs
"""

from google_play_scraper import search
import sys


def search_apps(search_terms, country='et', lang='en'):
    """
    Search for apps on Google Play Store
    
    Args:
        search_terms (list): List of search terms to try
        country (str): Country code (default: 'et' for Ethiopia)
        lang (str): Language code (default: 'en')
    """
    print("=" * 70)
    print("Google Play Store App ID Finder")
    print("=" * 70)
    
    all_results = []
    
    for term in search_terms:
        print(f"\nSearching for: '{term}'...")
        try:
            results = search(term, lang=lang, country=country, n_hits=5)
            
            if results:
                print(f"Found {len(results)} result(s):")
                for i, result in enumerate(results, 1):
                    print(f"\n  {i}. {result.get('title', 'Unknown')}")
                    print(f"     App ID: {result.get('appId', 'N/A')}")
                    print(f"     Developer: {result.get('developer', 'N/A')}")
                    print(f"     Rating: {result.get('score', 'N/A')}")
                    print(f"     Installs: {result.get('installs', 'N/A')}")
                    print(f"     URL: {result.get('url', 'N/A')}")
                    all_results.append(result)
            else:
                print(f"  No results found for '{term}'")
                
        except Exception as e:
            print(f"  Error searching for '{term}': {str(e)}")
    
    return all_results


def main():
    """
    Main function to search for bank apps
    """
    # Define search terms for each bank
    bank_searches = {
        'CBE': [
            'CBE Mobile Banking',
            'Commercial Bank of Ethiopia',
            'CBE Bank Ethiopia',
            'CBE mobile'
        ],
        'BOA': [
            'BOA Mobile Banking',
            'Bank of Abyssinia',
            'BOA Bank Ethiopia',
            'Abyssinia Bank mobile'
        ],
        'Dashen': [
            'Dashen Mobile Banking',
            'Dashen Bank',
            'Dashen Bank Ethiopia',
            'Dashen mobile'
        ]
    }
    
    print("\nThis script will help you find the correct app IDs for the three banks.")
    print("Please review the results and update scrape_reviews.py with the correct app IDs.\n")
    
    all_found_apps = {}
    
    for bank, search_terms in bank_searches.items():
        print("\n" + "=" * 70)
        print(f"Searching for {bank} apps")
        print("=" * 70)
        results = search_apps(search_terms)
        all_found_apps[bank] = results
    
    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print("\nTo update scrape_reviews.py, use the app IDs from the results above.")
    print("Look for the official mobile banking apps from each bank.")
    print("\nExample format for scrape_reviews.py:")
    print("""
BANK_APPS = {
    'CBE': {
        'app_id': 'com.cbe.mobilebanking',  # Replace with actual app ID
        'bank_name': 'Commercial Bank of Ethiopia',
        'app_name': 'CBE Mobile Banking'
    },
    ...
}
    """)


if __name__ == "__main__":
    main()

