# Interim Report: Fintech App Customer Experience Analysis

**Project:** Customer Experience Analytics for Fintech Apps  
**Banks Analyzed:** Commercial Bank of Ethiopia (CBE), Bank of Abyssinia (BOA), Dashen Bank  
**Date:** [Current Date]  
**Status:** In Progress

---

## Executive Summary

This project aims to analyze customer reviews from three major Ethiopian banks' mobile applications to identify satisfaction drivers, pain points, and improvement opportunities. The analysis involves data collection, sentiment analysis, thematic categorization, database storage, and actionable insights generation.

---

## Task 1: Data Collection and Preprocessing

### Objectives
- Scrape reviews from Google Play Store for three banks
- Collect minimum 400+ reviews per bank (1,200 total)
- Preprocess and clean data for analysis
- Establish proper Git workflow

### Requirements

#### Git Setup
- [ ] Create GitHub repository
- [ ] Include `.gitignore` file
- [ ] Include `requirements.txt` with dependencies
- [ ] Use "task-1" branch for development
- [ ] Commit frequently with meaningful messages

#### Web Scraping
- [ ] Use `google-play-scraper` library
- [ ] Collect reviews, ratings, dates, and app names
- [ ] Target minimum 400+ reviews per bank
- [ ] Total target: 1,200+ reviews

#### Preprocessing
- [ ] Remove duplicate reviews
- [ ] Handle missing data (<5% missing data target)
- [ ] Normalize dates to YYYY-MM-DD format
- [ ] Save as CSV with columns: `review`, `rating`, `date`, `bank`, `source`

### Key Performance Indicators (KPIs)
- [ ] 1,200+ reviews collected
- [ ] <5% missing data
- [ ] Clean CSV dataset
- [ ] Organized Git repo with clear commits

### Minimum Essential Deliverables
- [ ] Scrape at least 400 reviews per bank (1,200 total)
- [ ] Commit preprocessing script
- [ ] Update README.md with methodology

### Current Status
**Status:** [Not Started / In Progress / Completed]

**Progress Notes:**
- [Add your progress notes here]

**Challenges Encountered:**
- [Document any challenges]

**Next Steps:**
- [List immediate next steps]

---

## Task 2: Sentiment and Thematic Analysis

### Objectives
- Quantify review sentiment (positive, negative, neutral)
- Identify recurring themes and topics
- Uncover satisfaction drivers and pain points

### Requirements

#### Sentiment Analysis
- [ ] Use `distilbert-base-uncased-finetuned-sst-2-english` model
  - Alternative: Start with VADER or TextBlob for comparison
- [ ] Compute sentiment scores for all reviews
- [ ] Aggregate by bank and rating (e.g., mean sentiment for 1-star reviews)

#### Thematic Analysis
- [ ] Extract significant keywords and n-grams using TF-IDF or spaCy
  - Examples: "login error", "slow transfer", "good UI"
- [ ] Optionally employ topic modeling techniques
- [ ] Group keywords into 3-5 overarching themes per bank:
  - Account Access Issues
  - Transaction Performance
  - User Interface & Experience
  - Customer Support
  - Feature Requests
- [ ] Document grouping logic

#### Pipeline
- [ ] Preprocessing script (tokenization, stop-word removal, lemmatization)
- [ ] Save results as CSV with columns:
  - `review_id`, `review_text`, `sentiment_label`, `sentiment_score`, `identified_theme(s)`
- [ ] Extract keywords with spaCy or TF-IDF

#### Git Workflow
- [ ] Use "task-2" branch
- [ ] Commit analysis scripts
- [ ] Merge via pull request

### Key Performance Indicators (KPIs)
- [ ] Sentiment scores for 90%+ reviews
- [ ] 3+ themes per bank with examples
- [ ] Modular pipeline code

### Minimum Essential Deliverables
- [ ] Sentiment scores for 400 reviews
- [ ] 2 themes per bank via keywords
- [ ] Commit analysis script

### Current Status
**Status:** [Not Started / In Progress / Completed]

**Progress Notes:**
- [Add your progress notes here]

**Challenges Encountered:**
- [Document any challenges]

**Next Steps:**
- [List immediate next steps]

---

## Task 3: Store Cleaned Data in PostgreSQL

### Objectives
- Design and implement a relational database
- Store cleaned and processed review data persistently
- Simulate real-world data engineering workflows

### Requirements

#### PostgreSQL Database Setup
- [ ] Install PostgreSQL on system
- [ ] Create database named `bank_reviews`

#### Schema Design
- [ ] **Banks Table:**
  - `bank_id` (PRIMARY KEY)
  - `bank_name`
  - `app_name`

- [ ] **Reviews Table:**
  - `review_id` (PRIMARY KEY)
  - `bank_id` (FOREIGN KEY)
  - `review_text`
  - `rating`
  - `review_date`
  - `sentiment_label`
  - `sentiment_score`
  - `source`

#### Data Insertion
- [ ] Write Python script using `psycopg2` or `SQLAlchemy`
- [ ] Insert cleaned review data
- [ ] Write SQL queries to verify data integrity:
  - Count reviews per bank
  - Average rating per bank
  - Data quality checks

#### Documentation
- [ ] Document schema in README.md
- [ ] Commit SQL dump or schema file to GitHub

### Key Performance Indicators (KPIs)
- [ ] Working database connection + insert script
- [ ] Tables populated with >1,000 review entries
- [ ] SQL dump or schema file committed to GitHub

### Minimum Essential Deliverables
- [ ] PostgreSQL database created with both tables
- [ ] Python script that successfully inserts at least 400 reviews
- [ ] Schema documented in README.md

### Current Status
**Status:** [Not Started / In Progress / Completed]

**Progress Notes:**
- [Add your progress notes here]

**Challenges Encountered:**
- [Document any challenges]

**Next Steps:**
- [List immediate next steps]

---

## Task 4: Insights and Recommendations

### Objectives
- Derive actionable insights from sentiment and thematic analysis
- Visualize results effectively
- Recommend app improvements

### Requirements

#### Insights Generation
- [ ] Identify 2+ satisfaction drivers per bank (e.g., fast navigation)
- [ ] Identify 2+ pain points per bank (e.g., crashes)
- [ ] Compare banks (e.g., CBE vs. BOA vs. Dashen)
- [ ] Suggest 2+ improvements per bank (e.g., add budgeting tool)

#### Visualization
- [ ] Create 3-5 plots using Matplotlib/Seaborn:
  - Sentiment trends over time
  - Rating distributions
  - Keyword clouds (word clouds)
  - Theme frequency charts
  - Bank comparison charts

#### Ethics and Bias Considerations
- [ ] Note potential review biases (e.g., negative skew)
- [ ] Acknowledge limitations of the analysis

#### Git Workflow
- [ ] Use "task-4" branch
- [ ] Commit visuals and reports
- [ ] Merge via pull request

### Key Performance Indicators (KPIs)
- [ ] 2+ drivers/pain points with evidence
- [ ] Clear, labeled visualizations
- [ ] Practical recommendations

### Minimum Essential Deliverables
- [ ] 1 driver, 1 pain point per bank
- [ ] 2 plots (e.g., sentiment bar, keyword chart)
- [ ] 4-page final report

### Current Status
**Status:** [Not Started / In Progress / Completed]

**Progress Notes:**
- [Add your progress notes here]

**Challenges Encountered:**
- [Document any challenges]

**Next Steps:**
- [List immediate next steps]

---

## Overall Project Progress

### Completion Status
- **Task 1:** [ ] 0% | [ ] 25% | [ ] 50% | [ ] 75% | [ ] 100%
- **Task 2:** [ ] 0% | [ ] 25% | [ ] 50% | [ ] 75% | [ ] 100%
- **Task 3:** [ ] 0% | [ ] 25% | [ ] 50% | [ ] 75% | [ ] 100%
- **Task 4:** [ ] 0% | [ ] 25% | [ ] 50% | [ ] 75% | [ ] 100%

**Overall Project Completion:** [ ] 0% | [ ] 25% | [ ] 50% | [ ] 75% | [ ] 100%

### Timeline
- **Start Date:** [To be filled]
- **Target Completion Date:** [To be filled]
- **Current Date:** [To be filled]

### Key Achievements
- [List major achievements so far]

### Blockers and Risks
- [List any blockers or risks]

### Next Milestones
1. [Milestone 1]
2. [Milestone 2]
3. [Milestone 3]

---

## Technical Stack

### Libraries and Tools
- **Web Scraping:** `google-play-scraper`
- **Data Processing:** `pandas`, `numpy`
- **NLP:** `transformers` (Hugging Face), `spacy`, `nltk`, `VADER`, `TextBlob`
- **Database:** `PostgreSQL`, `psycopg2` or `SQLAlchemy`
- **Visualization:** `matplotlib`, `seaborn`, `wordcloud`
- **Version Control:** `Git`, `GitHub`

### Dependencies
[To be updated in requirements.txt]

---

## Methodology

### Data Collection Approach
[Describe your approach to scraping reviews]

### Preprocessing Pipeline
[Describe your preprocessing steps]

### Sentiment Analysis Methodology
[Describe your sentiment analysis approach]

### Thematic Analysis Methodology
[Describe how you identify and group themes]

### Database Design Rationale
[Explain your database schema design decisions]

---

## Deliverables Checklist

### Code and Scripts
- [ ] Web scraping script
- [ ] Data preprocessing script
- [ ] Sentiment analysis script
- [ ] Thematic analysis script
- [ ] Database insertion script
- [ ] Visualization scripts

### Data Files
- [ ] Raw scraped data (CSV)
- [ ] Cleaned and preprocessed data (CSV)
- [ ] Processed data with sentiment and themes (CSV)
- [ ] Database schema file
- [ ] SQL dump file

### Documentation
- [ ] README.md with methodology
- [ ] Interim report (this document)
- [ ] Final report (4+ pages)
- [ ] Code comments and docstrings

### Git Repository
- [ ] `.gitignore` file
- [ ] `requirements.txt`
- [ ] Organized branch structure (task-1, task-2, task-3, task-4)
- [ ] Meaningful commit messages
- [ ] Pull requests for each task

### Visualizations
- [ ] Sentiment distribution charts
- [ ] Rating distribution charts
- [ ] Keyword/word clouds
- [ ] Theme frequency charts
- [ ] Bank comparison visualizations

---

## Notes and Observations

### Data Quality Observations
[Note any data quality issues or interesting patterns]

### Technical Challenges
[Document technical challenges and solutions]

### Insights Preview
[Early insights or patterns noticed]

---

## Appendix

### A. Bank App Information
- **CBE (Commercial Bank of Ethiopia):** [App name, package ID]
- **BOA (Bank of Abyssinia):** [App name, package ID]
- **Dashen Bank:** [App name, package ID]

### B. Useful Resources
- [Link to Google Play Store]
- [Link to documentation]
- [Other relevant resources]

### C. Contact Information
[If applicable]

---

**Report Last Updated:** [Date]  
**Next Review Date:** [Date]

