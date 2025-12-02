# Tasks 2, 3, and 4 Execution Guide

## Prerequisites

Before running Tasks 2-4, ensure you have:

1. **Data Collected**: Run Task 1 data collection first
   ```bash
   python scripts/scrape_reviews.py
   python scripts/clean_reviews.py
   ```

2. **Dependencies Installed**:
   ```bash
   pip install -r requirements.txt
   python -m nltk.downloader vader_lexicon
   ```

3. **PostgreSQL Setup** (for Task 3):
   - Install PostgreSQL
   - Create database: `CREATE DATABASE bank_reviews;`
   - Configure `configs/db.yaml` with your database credentials

## Task 2: Sentiment and Thematic Analysis

### Step 1: Run Sentiment Analysis
```bash
python scripts/run_analysis.py
```
This will:
- Load cleaned review data
- Compute sentiment scores using VADER
- Save results to `data/processed/reviews_with_sentiment.csv`

### Step 2: Run Thematic Analysis
```bash
python scripts/run_theme_extraction.py
```
This will:
- Extract keywords using TF-IDF
- Map keywords to themes (5 predefined themes)
- Save results to `data/processed/reviews_with_themes.csv`

### Expected Output
- CSV file with columns: `review_id`, `review_text`, `sentiment_label`, `sentiment_score`, `themes`, `keywords`
- Sentiment scores for 90%+ reviews
- 3+ themes per bank identified

## Task 3: PostgreSQL Database Storage

### Step 1: Configure Database
Edit `configs/db.yaml`:
```yaml
database:
  host: localhost
  port: 5432
  name: bank_reviews
  user: your_username
  password: your_password
```

### Step 2: Load Data
```bash
python scripts/load_to_postgres.py
```
This will:
- Create database schema (banks and reviews tables)
- Load processed review data
- Verify data integrity with SQL queries

### Expected Output
- Database with >1,000 review entries
- Data integrity verification results
- SQL queries showing review counts and average ratings per bank

## Task 4: Insights and Recommendations

### Run Report Generation
```bash
python scripts/generate_report.py
```
This will:
- Identify satisfaction drivers and pain points per bank
- Compare banks
- Generate 3-5 visualizations
- Create final report with recommendations

### Expected Output
- Visualizations in `reports/` directory:
  - `rating_distribution.png`
  - `sentiment_distribution.png`
  - `average_rating_comparison.png`
  - `wordcloud.png`
  - `theme_frequency.png`
- Final report: `reports/final_report.md`

## Running All Tasks Together

You can run all tasks sequentially:
```bash
python scripts/run_tasks_2_3_4.py
```

## Verification Checklist

### Task 2
- [ ] `reviews_with_sentiment.csv` created
- [ ] `reviews_with_themes.csv` created
- [ ] Sentiment scores for 90%+ reviews
- [ ] 3+ themes per bank identified

### Task 3
- [ ] PostgreSQL database created
- [ ] Tables populated with >1,000 reviews
- [ ] Data integrity verified
- [ ] Schema file committed to GitHub

### Task 4
- [ ] 2+ drivers and pain points per bank identified
- [ ] 3-5 visualizations created
- [ ] Final report generated (10+ pages)
- [ ] Recommendations provided per bank

## Troubleshooting

### No Data Found
If you get "No data found" errors:
1. Run Task 1 data collection first
2. Check that files exist in `data/processed/` or `data/interim/`

### Database Connection Issues
If PostgreSQL connection fails:
1. Ensure PostgreSQL is running: `pg_isready`
2. Check database credentials in `configs/db.yaml`
3. Verify database exists: `psql -l | grep bank_reviews`

### Missing Dependencies
If import errors occur:
```bash
pip install -r requirements.txt
python -m nltk.downloader vader_lexicon punkt stopwords
```

