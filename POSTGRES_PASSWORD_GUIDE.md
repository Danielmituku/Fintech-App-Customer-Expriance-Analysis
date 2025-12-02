# PostgreSQL Password Guide

## Finding or Resetting Your PostgreSQL Password

### Method 1: Check if you have a saved password

```bash
# Check for .pgpass file (saved passwords)
cat ~/.pgpass

# Check environment variables
echo $PGPASSWORD
```

### Method 2: Reset PostgreSQL Password (Recommended)

Since you installed PostgreSQL via Homebrew, try these steps:

#### Step 1: Stop PostgreSQL
```bash
brew services stop postgresql@14
# or
brew services stop postgresql
```

#### Step 2: Start PostgreSQL in single-user mode (bypasses authentication)
```bash
# Find your data directory
ls -la /opt/homebrew/var/postgresql@14/
# or
ls -la /opt/homebrew/var/postgresql/

# Start in single-user mode (replace with your actual data directory)
/opt/homebrew/opt/postgresql@14/bin/postgres --single -D /opt/homebrew/var/postgresql@14/ postgres
```

#### Step 3: In the postgres prompt, run:
```sql
ALTER USER postgres WITH PASSWORD 'password';
\q
```

#### Step 4: Restart PostgreSQL normally
```bash
brew services start postgresql@14
```

### Method 3: Use Trust Authentication (Easier for Development)

Edit PostgreSQL's authentication config to allow local connections without password:

#### Step 1: Find pg_hba.conf
```bash
# For Homebrew PostgreSQL
find /opt/homebrew/var/postgresql* -name "pg_hba.conf" 2>/dev/null
# or
/opt/homebrew/opt/postgresql@14/share/postgresql@14/pg_hba.conf.sample
```

#### Step 2: Edit pg_hba.conf
The file is usually at: `/opt/homebrew/var/postgresql@14/pg_hba.conf`

Change this line:
```
host    all             all             127.0.0.1/32            scram-sha-256
```

To:
```
host    all             all             127.0.0.1/32            trust
```

Also change:
```
local   all             all                                     scram-sha-256
```

To:
```
local   all             all                                     trust
```

#### Step 3: Reload PostgreSQL
```bash
brew services restart postgresql@14
```

Now you can connect without a password!

### Method 4: Quick Solution - Set a Simple Password

If you can access psql somehow, run:

```sql
ALTER USER postgres PASSWORD 'password';
```

Or create a new superuser:
```sql
CREATE USER postgres WITH SUPERUSER PASSWORD 'password';
```

## Recommended Quick Fix

**For development purposes, I recommend Method 3 (trust authentication)** - it's the easiest and you won't need to remember passwords.

After enabling trust auth, update `configs/db.yaml`:
```yaml
postgres:
  user: "postgres"
  password: ""  # Empty string for trust auth
```

## Verify Connection

After setting up, test:
```bash
psql -U postgres -d postgres -c "SELECT version();"
```

If it works, you're all set!

