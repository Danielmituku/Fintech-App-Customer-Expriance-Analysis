# Simple PostgreSQL Password Fix

## The Issue
PostgreSQL is asking for a password but you don't know what it is.

## Easiest Solution: Set Password via psql

**Option 1: If you can access psql somehow**

Try connecting and when prompted for password, try:
- `postgres` (common default)
- `password` 
- `admin`
- Just press Enter (empty password)

Once connected, run:
```sql
ALTER USER postgres WITH PASSWORD 'password';
CREATE DATABASE bank_reviews;
```

**Option 2: Use PGPASSWORD environment variable**

```bash
export PGPASSWORD='password'
psql -U postgres -c "ALTER USER postgres WITH PASSWORD 'password';"
psql -U postgres -c "CREATE DATABASE bank_reviews;"
unset PGPASSWORD
```

**Option 3: Reset PostgreSQL (Nuclear Option)**

If nothing works, reset PostgreSQL:

```bash
# Stop PostgreSQL
brew services stop postgresql@14

# Remove data directory (WARNING: Deletes all databases!)
rm -rf /opt/homebrew/var/postgresql@14

# Reinitialize
initdb /opt/homebrew/var/postgresql@14

# Start PostgreSQL
brew services start postgresql@14

# Now connect without password and set one
psql -U $(whoami) -d postgres
# In psql:
ALTER USER postgres WITH PASSWORD 'password';
CREATE DATABASE bank_reviews;
```

## After Setting Password

1. Update `configs/db.yaml`:
   ```yaml
   password: "password"  # The password you just set
   ```

2. Run the setup:
   ```bash
   python scripts/setup_database.py
   python scripts/load_to_postgres.py
   ```

## Quick Test

Test your connection:
```bash
PGPASSWORD='password' psql -U postgres -d postgres -c "SELECT version();"
```

If this works, you're all set!

