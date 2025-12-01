# Fintech App Customer Experience Analysis

Customer Experience Analytics for Fintech Apps: Commercial Bank of Ethiopia (CBE), Bank of Abyssinia (BOA), and Dashen Bank

## Project Overview

This project analyzes customer reviews from three major Ethiopian banks' mobile applications to identify:
- Satisfaction drivers and pain points
- Sentiment trends across different banks
- Thematic patterns in user feedback
- Actionable recommendations for app improvements

## Banks Analyzed

1. **Commercial Bank of Ethiopia (CBE)**
2. **Bank of Abyssinia (BOA)**
3. **Dashen Bank**

## Project Structure

```
Fintech-App-Customer-Expriance-Analysis/
├── README.md                 # This file
├── INTERIM_REPORT.md         # Progress tracking and task documentation
├── .gitignore               # Git ignore rules
├── requirements.txt         # Python dependencies
├── data/                    # Data files (to be created)
│   ├── raw/                # Raw scraped data
│   ├── processed/          # Cleaned and processed data
│   └── results/            # Analysis results
├── scripts/                 # Analysis scripts (to be created)
│   ├── scraping/           # Web scraping scripts
│   ├── preprocessing/      # Data preprocessing scripts
│   ├── analysis/           # Sentiment and thematic analysis
│   ├── database/           # Database setup and insertion scripts
│   └── visualization/      # Visualization scripts
└── reports/                 # Generated reports (to be created)
```

## Tasks

### Task 1: Data Collection and Preprocessing
- Scrape reviews from Google Play Store
- Collect 400+ reviews per bank (1,200+ total)
- Preprocess and clean data

### Task 2: Sentiment and Thematic Analysis
- Perform sentiment analysis using transformer models
- Identify themes and topics
- Extract keywords and n-grams

### Task 3: Store Cleaned Data in PostgreSQL
- Design database schema
- Store processed data in PostgreSQL
- Verify data integrity

### Task 4: Insights and Recommendations
- Generate actionable insights
- Create visualizations
- Provide recommendations

For detailed task requirements and progress tracking, see [INTERIM_REPORT.md](INTERIM_REPORT.md).

## Setup Instructions

### Prerequisites
- Python 3.8+
- PostgreSQL 12+
- Git

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Fintech-App-Customer-Expriance-Analysis
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Download spaCy language model:
```bash
python -m spacy download en_core_web_sm
```

5. Download NLTK data (if needed):
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')
```

### Database Setup

1. Install PostgreSQL on your system
2. Create the database:
```sql
CREATE DATABASE bank_reviews;
```

3. Configure database connection (create `.env` file):
```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=bank_reviews
DB_USER=your_username
DB_PASSWORD=your_password
```

## Usage

[To be updated as scripts are developed]

## Methodology

[To be updated with detailed methodology as work progresses]

## Progress Tracking

See [INTERIM_REPORT.md](INTERIM_REPORT.md) for detailed progress tracking, task checklists, and status updates.

## Contributing

This is a project for 10Academy Week 2 assignment. Follow the branch structure:
- `task-1`: Data collection and preprocessing
- `task-2`: Sentiment and thematic analysis
- `task-3`: Database storage
- `task-4`: Insights and recommendations

## License

[To be determined]

## Contact

[Your contact information]
