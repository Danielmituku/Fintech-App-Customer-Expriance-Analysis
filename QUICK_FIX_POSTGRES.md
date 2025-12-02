# Quick Fix: PostgreSQL Password Issue

## The Problem
PostgreSQL is asking for a password but you don't know what it is.

## Solution Options

### Option 1: Set Password via Environment Variable (Easiest)

Create a `.env` file or export the password:

```bash
export PGPASSWORD='password'
psql -U postgres -c "ALTER USER postgres WITH PASSWORD 'password';"
unset PGPASSWORD
```

Then update `configs/db.yaml`:
```yaml
password: "password"
```

### Option 2: Use createdb command (Bypasses user creation)

```bash
createdb bank_reviews
```

Then update `configs/db.yaml` to use your macOS username:
```yaml
user: "danielmituku"
password: ""
```

### Option 3: Reset via Homebrew

```bash
# Stop PostgreSQL
brew services stop postgresql@14

# Remove and reinitialize (WARNING: This deletes all data!)
rm -rf /opt/homebrew/var/postgresql@14
initdb /opt/homebrew/var/postgresql@14

# Start PostgreSQL
brew services start postgresql@14

# Now connect without password and set one
psql -U $(whoami) -d postgres
# In psql:
ALTER USER postgres WITH PASSWORD 'password';
```

### Option 4: Try Common Default Passwords

Try these common defaults:
- `postgres`
- `password`
- `admin`
- `root`
- (empty/blank)

Update `configs/db.yaml` and test:
```bash
python scripts/setup_database.py
```

## Recommended: Try Option 2 First

Use `createdb` which might work with your macOS user:

```bash
createdb bank_reviews
```

Then update the config to use your username instead of postgres.

