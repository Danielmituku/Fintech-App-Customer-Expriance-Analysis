# Google Play Store App IDs

This document contains instructions for finding the correct Google Play Store app IDs for the three banks.

## How to Find App IDs

1. Go to Google Play Store (https://play.google.com/store)
2. Search for the bank's mobile banking app
3. Open the app page
4. The app ID is in the URL: `https://play.google.com/store/apps/details?id=APP_ID_HERE`

## Bank Apps

### Commercial Bank of Ethiopia (CBE)
- **Search terms:** "CBE Mobile Banking", "Commercial Bank of Ethiopia"
- **App ID:** [To be updated]
- **URL:** [To be updated]

### Bank of Abyssinia (BOA)
- **Search terms:** "BOA Mobile Banking", "Bank of Abyssinia"
- **App ID:** [To be updated]
- **URL:** [To be updated]

### Dashen Bank
- **Search terms:** "Dashen Mobile Banking", "Dashen Bank"
- **App ID:** [To be updated]
- **URL:** [To be updated]

## Updating App IDs

Once you find the correct app IDs:

1. Open `scripts/scraping/scrape_reviews.py`
2. Update the `BANK_APPS` dictionary with the correct app IDs
3. Save and run the scraping script

## Example

If the app URL is: `https://play.google.com/store/apps/details?id=com.example.bankapp`

Then the app ID is: `com.example.bankapp`

## Alternative Method

You can also use the `google-play-scraper` library to search for apps:

```python
from google_play_scraper import search

results = search("CBE Mobile Banking", lang='en', country='et')
for result in results:
    print(f"Title: {result['title']}")
    print(f"App ID: {result['appId']}")
    print(f"URL: {result['url']}")
    print("-" * 50)
```

