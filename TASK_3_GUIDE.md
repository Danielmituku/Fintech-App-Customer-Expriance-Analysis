# Task 3: PostgreSQL Database Storage - Setup Guide

## Prerequisites

1. **PostgreSQL Installed**: Make sure PostgreSQL is installed on your system
   - macOS: `brew install postgresql@14` or download from postgresql.org
   - Linux: `sudo apt-get install postgresql` (Ubuntu/Debian)
   - Windows: Download installer from postgresql.org

2. **PostgreSQL Running**: 
   ```bash
   # Check if PostgreSQL is running
   pg_isready
   
   # Start PostgreSQL (macOS with Homebrew)
   brew services start postgresql@14
   
   # Start PostgreSQL (Linux)
   sudo systemctl start postgresql
   ```

3. **Dependencies Installed**:
   ```bash
   pip install psycopg2-binary
   ```

## Step-by-Step Setup

### Step 1: Configure Database Credentials

Edit `configs/db.yaml` and update with your PostgreSQL credentials:

```yaml
postgres:
  host: "localhost"
  port: 5432
  database: "bank_reviews"  # Will be created automatically
  user: "postgres"           # Your PostgreSQL username
  password: "your_password"  # Your PostgreSQL password
```

### Step 2: Create Database

Run the setup script to create the database:

```bash
source venv/bin/activate
python scripts/setup_database.py
```

This will:
- Create the `bank_reviews` database if it doesn't exist
- Verify connection to PostgreSQL

**Alternative (Manual)**:
```bash
psql -U postgres -c "CREATE DATABASE bank_reviews;"
```

### Step 3: Load Data into PostgreSQL

Once the database is created, load your processed review data:

```bash
python scripts/load_to_postgres.py
```

This will:
- Create the schema (banks and reviews tables)
- Load data from `data/processed/reviews_with_themes.csv`
- Insert banks and reviews with proper foreign key relationships
- Verify data integrity

### Step 4: Verify Data

The script will automatically run verification queries showing:
- Review counts per bank
- Average ratings per bank
- Sentiment distribution

You can also verify manually:

```bash
psql -U postgres -d bank_reviews -c "SELECT * FROM review_statistics;"
```

## Database Schema

### Banks Table
- `bank_id` (PRIMARY KEY, SERIAL)
- `bank_name` (VARCHAR, UNIQUE)
- `app_name` (VARCHAR)

### Reviews Table
- `review_id` (PRIMARY KEY, VARCHAR)
- `bank_id` (FOREIGN KEY → banks.bank_id)
- `review_text` (TEXT)
- `rating` (INTEGER, 1-5)
- `review_date` (DATE)
- `sentiment_label` (VARCHAR)
- `sentiment_score` (FLOAT)
- `source` (VARCHAR, default: 'Google Play Store')
- `themes` (TEXT)
- `keywords` (TEXT)
- `created_at` (TIMESTAMP)

## Verification Queries

After loading data, you can run these SQL queries:

```sql
-- Count reviews per bank
SELECT b.bank_name, COUNT(r.review_id) as review_count
FROM banks b
LEFT JOIN reviews r ON b.bank_id = r.bank_id
GROUP BY b.bank_name;

-- Average rating per bank
SELECT b.bank_name, AVG(r.rating) as avg_rating
FROM banks b
JOIN reviews r ON b.bank_id = r.bank_id
GROUP BY b.bank_name;

-- Sentiment distribution
SELECT sentiment_label, COUNT(*) as count
FROM reviews
WHERE sentiment_label IS NOT NULL
GROUP BY sentiment_label;

-- Use the view
SELECT * FROM review_statistics;
```

## Troubleshooting

### Connection Errors
- **Error: "connection refused"**: PostgreSQL is not running
  - Start PostgreSQL service
  - Check port 5432 is not blocked

- **Error: "authentication failed"**: Wrong password
  - Update password in `configs/db.yaml`
  - Or reset PostgreSQL password: `psql -U postgres -c "ALTER USER postgres PASSWORD 'newpassword';"`

### Database Creation Errors
- **Error: "database already exists"**: Database already created, skip to Step 3
- **Error: "permission denied"**: Need superuser privileges
  - Use `postgres` user or a user with CREATEDB privilege

### Data Loading Errors
- **Error: "relation does not exist"**: Schema not created
  - Check `src/fintech_app_reviews/db/schema.sql` exists
  - Run setup again

- **Error: "duplicate key"**: Data already loaded
  - The script uses UPSERT, so it's safe to run multiple times
  - Or truncate tables: `TRUNCATE reviews, banks CASCADE;`

## Expected Results

After successful execution:
- ✅ Database `bank_reviews` created
- ✅ Tables `banks` and `reviews` created with proper schema
- ✅ >1,000 review entries loaded (we have 1,167)
- ✅ Data integrity verified
- ✅ Foreign key relationships working

## Files Created

- `src/fintech_app_reviews/db/schema.sql` - Database schema
- Database tables in PostgreSQL
- Logs in `logs/db_loader.log` (if configured)

## Next Steps

After Task 3 is complete:
1. Commit the schema.sql file to GitHub
2. Document the schema in README.md
3. Proceed to Task 4 (if not already done)

