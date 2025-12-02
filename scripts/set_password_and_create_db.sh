#!/bin/bash
# Quick script to set PostgreSQL password and create database

echo "Setting PostgreSQL password for 'postgres' user..."
echo "You'll need to enter the password when prompted."

# Method 1: Try to set password using PGPASSWORD
read -sp "Enter your PostgreSQL password (or press Enter to set a new one): " PASSWORD
echo ""

if [ -z "$PASSWORD" ]; then
    echo "Setting password to 'password'..."
    PASSWORD="password"
fi

# Export password for this session
export PGPASSWORD="$PASSWORD"

# Try to create database
echo "Creating database 'bank_reviews'..."
createdb -U postgres bank_reviews 2>&1

if [ $? -eq 0 ]; then
    echo "✓ Database 'bank_reviews' created successfully!"
    echo ""
    echo "Update configs/db.yaml with:"
    echo "  password: \"$PASSWORD\""
else
    echo "Failed to create database. Trying to set password first..."
    echo ""
    echo "Please run this manually:"
    echo "  psql -U postgres"
    echo "  Then in psql, run: ALTER USER postgres WITH PASSWORD 'password';"
    echo "  Then: CREATE DATABASE bank_reviews;"
fi

unset PGPASSWORD

