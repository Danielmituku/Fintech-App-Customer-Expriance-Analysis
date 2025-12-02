-- PostgreSQL Schema for Bank Reviews Database
-- Task 3: Store Cleaned Data in PostgreSQL

-- Create Banks Table
CREATE TABLE IF NOT EXISTS banks (
    bank_id SERIAL PRIMARY KEY,
    bank_name VARCHAR(255) NOT NULL UNIQUE,
    app_name VARCHAR(255)
);

-- Create Reviews Table
CREATE TABLE IF NOT EXISTS reviews (
    review_id VARCHAR(255) PRIMARY KEY,
    bank_id INTEGER NOT NULL REFERENCES banks(bank_id) ON DELETE CASCADE,
    review_text TEXT,
    rating INTEGER CHECK (rating >= 1 AND rating <= 5),
    review_date DATE,
    sentiment_label VARCHAR(50),
    sentiment_score FLOAT,
    source VARCHAR(100) DEFAULT 'Google Play Store',
    themes TEXT,
    keywords TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for better query performance
CREATE INDEX IF NOT EXISTS idx_reviews_bank_id ON reviews(bank_id);
CREATE INDEX IF NOT EXISTS idx_reviews_rating ON reviews(rating);
CREATE INDEX IF NOT EXISTS idx_reviews_sentiment_label ON reviews(sentiment_label);
CREATE INDEX IF NOT EXISTS idx_reviews_review_date ON reviews(review_date);

-- Create view for review statistics
CREATE OR REPLACE VIEW review_statistics AS
SELECT 
    b.bank_name,
    COUNT(r.review_id) as total_reviews,
    AVG(r.rating) as average_rating,
    COUNT(CASE WHEN r.sentiment_label = 'positive' THEN 1 END) as positive_count,
    COUNT(CASE WHEN r.sentiment_label = 'negative' THEN 1 END) as negative_count,
    COUNT(CASE WHEN r.sentiment_label = 'neutral' THEN 1 END) as neutral_count
FROM banks b
LEFT JOIN reviews r ON b.bank_id = r.bank_id
GROUP BY b.bank_id, b.bank_name;

