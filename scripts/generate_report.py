#!/usr/bin/env python3
"""
Task 4: Generate Insights, Visualizations, and Recommendations
"""

import logging
import os
import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)


def load_data():
    """Load processed data with sentiment and themes"""
    input_files = [
        "data/processed/reviews_with_themes.csv",
        "data/processed/reviews_with_sentiment.csv",
        "data/processed/reviews.csv"
    ]
    
    for file in input_files:
        if os.path.exists(file):
            df = pd.read_csv(file)
            logger.info(f"Loaded {len(df)} reviews from {file}")
            return df
    
    raise FileNotFoundError("No processed data file found. Run Task 2 first.")


def identify_drivers_and_pain_points(df):
    """Identify satisfaction drivers and pain points per bank"""
    results = {}
    
    # Map column names
    bank_col = 'bank' if 'bank' in df.columns else 'bank_name'
    rating_col = 'rating' if 'rating' in df.columns else 'score'
    sentiment_col = 'sentiment_label' if 'sentiment_label' in df.columns else 'sentiment'
    themes_col = 'themes' if 'themes' in df.columns else 'theme'
    review_col = 'review_text' if 'review_text' in df.columns else 'review'
    
    for bank in df[bank_col].unique():
        bank_df = df[df[bank_col] == bank]
        
        # Drivers: High ratings (4-5 stars) with positive sentiment
        high_rated = bank_df[bank_df[rating_col] >= 4]
        positive_reviews = high_rated[high_rated[sentiment_col] == 'positive']
        
        # Extract common themes/keywords from positive reviews
        drivers = []
        if themes_col in positive_reviews.columns:
            theme_counts = positive_reviews[themes_col].str.split('|').explode().value_counts()
            drivers = theme_counts.head(3).index.tolist()
        
        # Pain points: Low ratings (1-2 stars) with negative sentiment
        low_rated = bank_df[bank_df[rating_col] <= 2]
        negative_reviews = low_rated[low_rated[sentiment_col] == 'negative']
        
        pain_points = []
        if themes_col in negative_reviews.columns:
            theme_counts = negative_reviews[themes_col].str.split('|').explode().value_counts()
            pain_points = theme_counts.head(3).index.tolist()
        
        results[bank] = {
            'drivers': drivers,
            'pain_points': pain_points,
            'avg_rating': bank_df[rating_col].mean(),
            'positive_pct': (bank_df[sentiment_col] == 'positive').sum() / len(bank_df) * 100
        }
    
    return results


def create_visualizations(df, output_dir="reports"):
    """Create visualizations for the report"""
    os.makedirs(output_dir, exist_ok=True)
    
    # Map column names
    bank_col = 'bank' if 'bank' in df.columns else 'bank_name'
    rating_col = 'rating' if 'rating' in df.columns else 'score'
    sentiment_col = 'sentiment_label' if 'sentiment_label' in df.columns else 'sentiment'
    review_col = 'review_text' if 'review_text' in df.columns else 'review'
    
    # 1. Rating Distribution by Bank
    plt.figure(figsize=(12, 6))
    rating_counts = df.groupby([bank_col, rating_col]).size().unstack(fill_value=0)
    rating_counts.plot(kind='bar', stacked=True, colormap='RdYlGn')
    plt.title('Rating Distribution by Bank', fontsize=16, fontweight='bold')
    plt.xlabel('Bank', fontsize=12)
    plt.ylabel('Number of Reviews', fontsize=12)
    plt.legend(title='Rating', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig(f"{output_dir}/rating_distribution.png", dpi=300, bbox_inches='tight')
    plt.close()
    logger.info("✓ Created rating distribution chart")
    
    # 2. Sentiment Distribution by Bank
    plt.figure(figsize=(12, 6))
    sentiment_counts = df.groupby([bank_col, sentiment_col]).size().unstack(fill_value=0)
    sentiment_counts.plot(kind='bar', colormap='Set2')
    plt.title('Sentiment Distribution by Bank', fontsize=16, fontweight='bold')
    plt.xlabel('Bank', fontsize=12)
    plt.ylabel('Number of Reviews', fontsize=12)
    plt.legend(title='Sentiment', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig(f"{output_dir}/sentiment_distribution.png", dpi=300, bbox_inches='tight')
    plt.close()
    logger.info("✓ Created sentiment distribution chart")
    
    # 3. Average Rating Comparison
    plt.figure(figsize=(10, 6))
    avg_ratings = df.groupby(bank_col)[rating_col].mean().sort_values(ascending=False)
    avg_ratings.plot(kind='barh', color='steelblue')
    plt.title('Average Rating by Bank', fontsize=16, fontweight='bold')
    plt.xlabel('Average Rating', fontsize=12)
    plt.ylabel('Bank', fontsize=12)
    plt.xlim(0, 5)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/average_rating_comparison.png", dpi=300, bbox_inches='tight')
    plt.close()
    logger.info("✓ Created average rating comparison chart")
    
    # 4. Word Cloud (if review text available)
    if review_col in df.columns:
        try:
            all_text = ' '.join(df[review_col].fillna('').astype(str))
            wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_text)
            plt.figure(figsize=(16, 8))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis('off')
            plt.title('Word Cloud of All Reviews', fontsize=16, fontweight='bold', pad=20)
            plt.tight_layout()
            plt.savefig(f"{output_dir}/wordcloud.png", dpi=300, bbox_inches='tight')
            plt.close()
            logger.info("✓ Created word cloud")
        except Exception as e:
            logger.warning(f"Could not create word cloud: {e}")
    
    # 5. Theme Frequency by Bank (if themes available)
    if 'themes' in df.columns:
        try:
            theme_data = []
            for bank in df[bank_col].unique():
                bank_df = df[df[bank_col] == bank]
                themes = bank_df['themes'].str.split('|').explode()
                theme_counts = themes.value_counts().head(5)
                for theme, count in theme_counts.items():
                    if theme and theme.strip():
                        theme_data.append({'Bank': bank, 'Theme': theme, 'Count': count})
            
            if theme_data:
                theme_df = pd.DataFrame(theme_data)
                plt.figure(figsize=(14, 8))
                theme_pivot = theme_df.pivot(index='Theme', columns='Bank', values='Count').fillna(0)
                theme_pivot.plot(kind='barh', colormap='viridis')
                plt.title('Top Themes by Bank', fontsize=16, fontweight='bold')
                plt.xlabel('Number of Reviews', fontsize=12)
                plt.ylabel('Theme', fontsize=12)
                plt.legend(title='Bank', bbox_to_anchor=(1.05, 1), loc='upper left')
                plt.tight_layout()
                plt.savefig(f"{output_dir}/theme_frequency.png", dpi=300, bbox_inches='tight')
                plt.close()
                logger.info("✓ Created theme frequency chart")
        except Exception as e:
            logger.warning(f"Could not create theme frequency chart: {e}")


def generate_recommendations(insights):
    """Generate recommendations based on insights"""
    recommendations = {}
    
    for bank, data in insights.items():
        recs = []
        
        # Recommendations based on pain points
        for pain_point in data['pain_points']:
            if 'Account Access' in pain_point:
                recs.append("Improve authentication system: Implement biometric login and password recovery options")
            elif 'Transaction' in pain_point:
                recs.append("Optimize transaction processing: Reduce loading times and improve error handling")
            elif 'UI' in pain_point or 'Interface' in pain_point:
                recs.append("Enhance user interface: Simplify navigation and improve visual design")
            elif 'Support' in pain_point:
                recs.append("Strengthen customer support: Reduce response times and improve chat/call center availability")
            elif 'Feature' in pain_point:
                recs.append("Prioritize feature development: Address most requested features based on user feedback")
        
        # General recommendations
        if data['positive_pct'] < 50:
            recs.append("Focus on improving overall user satisfaction: Address common complaints systematically")
        
        if data['avg_rating'] < 3.5:
            recs.append("Conduct user research: Identify root causes of low ratings and prioritize fixes")
        
        recommendations[bank] = recs[:3]  # Top 3 recommendations
    
    return recommendations


def write_final_report(insights, recommendations, output_file="reports/final_report.md"):
    """Write the final report"""
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    with open(output_file, 'w') as f:
        f.write("# Fintech App Customer Experience Analysis - Final Report\n\n")
        f.write("## Executive Summary\n\n")
        f.write("This report analyzes customer reviews from three Ethiopian banks' mobile applications ")
        f.write("to identify satisfaction drivers, pain points, and improvement opportunities.\n\n")
        
        f.write("## Key Insights\n\n")
        
        for bank, data in insights.items():
            f.write(f"### {bank}\n\n")
            f.write(f"**Average Rating:** {data['avg_rating']:.2f}/5.0\n\n")
            f.write(f"**Positive Sentiment:** {data['positive_pct']:.1f}%\n\n")
            
            f.write("**Satisfaction Drivers:**\n")
            for driver in data['drivers']:
                f.write(f"- {driver}\n")
            f.write("\n")
            
            f.write("**Pain Points:**\n")
            for pain_point in data['pain_points']:
                f.write(f"- {pain_point}\n")
            f.write("\n")
        
        f.write("## Bank Comparison\n\n")
        f.write("| Bank | Avg Rating | Positive % | Top Driver | Top Pain Point |\n")
        f.write("|------|------------|------------|------------|----------------|\n")
        for bank, data in insights.items():
            top_driver = data['drivers'][0] if data['drivers'] else "N/A"
            top_pain = data['pain_points'][0] if data['pain_points'] else "N/A"
            f.write(f"| {bank} | {data['avg_rating']:.2f} | {data['positive_pct']:.1f}% | {top_driver} | {top_pain} |\n")
        f.write("\n")
        
        f.write("## Recommendations\n\n")
        for bank, recs in recommendations.items():
            f.write(f"### {bank}\n\n")
            for i, rec in enumerate(recs, 1):
                f.write(f"{i}. {rec}\n")
            f.write("\n")
        
        f.write("## Visualizations\n\n")
        f.write("See the following visualizations in the reports/ directory:\n")
        f.write("- rating_distribution.png: Rating distribution by bank\n")
        f.write("- sentiment_distribution.png: Sentiment analysis by bank\n")
        f.write("- average_rating_comparison.png: Average rating comparison\n")
        f.write("- wordcloud.png: Word cloud of all reviews\n")
        f.write("- theme_frequency.png: Theme frequency by bank\n\n")
        
        f.write("## Ethics and Bias Considerations\n\n")
        f.write("**Potential Review Biases:**\n")
        f.write("- Negative bias: Users with negative experiences are more likely to leave reviews\n")
        f.write("- Recency bias: Recent reviews may not reflect long-term app performance\n")
        f.write("- Selection bias: Only users who download and use the app can review it\n")
        f.write("- Language bias: Analysis focuses on English reviews, may miss local language feedback\n\n")
        f.write("**Limitations:**\n")
        f.write("- Analysis based on publicly available reviews only\n")
        f.write("- Sentiment analysis may not capture context-specific nuances\n")
        f.write("- Theme classification is rule-based and may miss emerging themes\n")
    
    logger.info(f"✓ Final report written to {output_file}")


def main():
    """Main function to generate insights and report"""
    logger.info("=" * 70)
    logger.info("TASK 4: Generate Insights and Recommendations")
    logger.info("=" * 70)
    
    try:
        # Load data
        df = load_data()
        
        # Identify drivers and pain points
        logger.info("\nIdentifying drivers and pain points...")
        insights = identify_drivers_and_pain_points(df)
        
        # Generate recommendations
        logger.info("Generating recommendations...")
        recommendations = generate_recommendations(insights)
        
        # Create visualizations
        logger.info("\nCreating visualizations...")
        create_visualizations(df)
        
        # Write final report
        logger.info("Writing final report...")
        write_final_report(insights, recommendations)
        
        logger.info("\n✓ TASK 4 COMPLETED SUCCESSFULLY")
        logger.info("Check the reports/ directory for visualizations and final_report.md")
        
    except Exception as e:
        logger.error(f"✗ Task 4 failed: {e}")
        raise


if __name__ == "__main__":
    main()

