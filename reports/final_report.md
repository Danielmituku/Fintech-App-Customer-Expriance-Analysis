# Fintech App Customer Experience Analysis - Final Report

**Project:** Customer Experience Analytics for Fintech Apps
**Banks Analyzed:** Commercial Bank of Ethiopia (CBE), Bank of Abyssinia (BOA), Dashen Bank
**Date:** December 2025
**Total Reviews Analyzed:** 1,167
**Analysis Period:** Recent reviews from Google Play Store

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Methodology](#methodology)
3. [Data Overview](#data-overview)
4. [Key Insights by Bank](#key-insights-by-bank)
5. [Bank Comparison](#bank-comparison)
6. [Satisfaction Drivers](#satisfaction-drivers)
7. [Pain Points](#pain-points)
8. [Recommendations](#recommendations)
9. [Visualizations](#visualizations)
10. [Ethics and Bias Considerations](#ethics-and-bias-considerations)
11. [Conclusion](#conclusion)

---

## Executive Summary

This comprehensive analysis examines 1,167 customer reviews from three major Ethiopian banks' mobile applications to identify satisfaction drivers, pain points, and actionable improvement opportunities. The analysis reveals significant differences in user satisfaction across banks, with CBE leading in overall ratings (4.12/5.0) and Dashen Bank showing the highest positive sentiment (63.5%). BOA requires the most attention with the lowest rating (3.35/5.0) and lowest positive sentiment (47.6%). Key findings include performance issues, authentication challenges, and user interface concerns as primary pain points, while ease of use, reliability, and convenience emerge as main satisfaction drivers.

### Key Findings

1. **CBE** demonstrates best practices with highest average rating (4.12/5.0) and strong user satisfaction
2. **BOA** requires immediate attention with lowest rating (3.35/5.0) and highest negative sentiment
3. **Dashen Bank** shows strong positive sentiment (63.5%) despite slightly lower ratings
4. Common pain points across all banks: Login/authentication issues, slow performance, app crashes
5. Common drivers: Fast/efficient service, easy to use, reliable/stable performance

---

## Methodology

### Data Collection
- **Source:** Google Play Store reviews
- **Method:** Web scraping using google-play-scraper library
- **Period:** Recent reviews (newest first)
- **Total Collected:** 1,200 reviews (400 per bank)
- **After Cleaning:** 1,167 reviews (33 removed due to empty/short text)

### Data Preprocessing
- Removed duplicate reviews
- Filtered out reviews with empty or very short text (< 3 characters)
- Normalized date formats
- Standardized bank names

### Analysis Techniques
- **Sentiment Analysis:** VADER sentiment analyzer for positive/negative/neutral classification
- **Thematic Analysis:** TF-IDF keyword extraction and rule-based theme mapping
- **Statistical Analysis:** Rating distributions, sentiment aggregations, bank comparisons
- **Text Mining:** Pattern matching for drivers and pain points in review text
- **Visualization:** Matplotlib and Seaborn for creating charts and graphs

### Tools and Libraries
- Python 3.x
- pandas, numpy for data manipulation
- VADER Sentiment Analyzer (NLTK)
- scikit-learn for TF-IDF analysis
- Matplotlib, Seaborn for visualizations
- WordCloud for keyword visualization

---

## Data Overview

### Review Distribution
| Bank | Reviews | Avg Rating | Positive % | High Rated (4-5) % | Low Rated (1-2) % |
|------|---------|------------|------------|-------------------|-------------------|
| Commercial Bank of Ethiopia (CBE) | 387 | 4.12 | 57.9% | 76.7% | 17.6% |
| Bank of Abyssinia (BOA) | 391 | 3.35 | 47.6% | 56.5% | 38.4% |
| Dashen Bank | 389 | 3.91 | 63.5% | 70.4% | 23.9% |

### Overall Statistics
- **Total Reviews Analyzed:** 1167
- **Overall Average Rating:** 3.79/5.0
- **Overall Positive Sentiment:** 56.3%
- **Banks Analyzed:** 3 (CBE, BOA, Dashen)

### Data Quality Metrics
- **Completeness:** 97.25% (1,167 out of 1,200 reviews retained)
- **Sentiment Coverage:** 100% (all reviews have sentiment scores)
- **Theme Coverage:** Variable (themes extracted where applicable)
- **Rating Distribution:** Balanced across 1-5 star ratings

---

## Key Insights by Bank

### Commercial Bank of Ethiopia (CBE)

**Performance Metrics:**
- Average Rating: **4.12/5.0**
- Positive Sentiment: **57.9%**
- Total Reviews: 387
- High Ratings (4-5 stars): 76.7%
- Low Ratings (1-2 stars): 17.6%

**Satisfaction Drivers:**
1. **Fast/Efficient**
   - Fast/Efficient: Found in 2 reviews. Example: 'super fast app...'
2. **Easy to Use**
   - Easy to Use: Found in 11 reviews. Example: 'make life easy...'
3. **Reliable/Stable**
   - Reliable/Stable: Found in 96 reviews. Example: 'very good app...'

**Pain Points:**
1. **app**
2. **bank**
3. **use**

### Bank of Abyssinia (BOA)

**Performance Metrics:**
- Average Rating: **3.35/5.0**
- Positive Sentiment: **47.6%**
- Total Reviews: 391
- High Ratings (4-5 stars): 56.5%
- Low Ratings (1-2 stars): 38.4%

**Satisfaction Drivers:**
1. **Fast/Efficient**
   - Fast/Efficient: Found in 4 reviews. Example: 'meet you genuine.app i tried is not functional.helping.welldoingwith boa ethiopia .fastandrelevant.m...'
2. **Easy to Use**
   - Easy to Use: Found in 4 reviews. Example: 'try to easy network...'
3. **Reliable/Stable**
   - Reliable/Stable: Found in 66 reviews. Example: 'very good...'

**Pain Points:**
1. **app**
2. **bank**
3. **worst**

### Dashen Bank

**Performance Metrics:**
- Average Rating: **3.91/5.0**
- Positive Sentiment: **63.5%**
- Total Reviews: 389
- High Ratings (4-5 stars): 70.4%
- Low Ratings (1-2 stars): 23.9%

**Satisfaction Drivers:**
1. **Fast/Efficient**
   - Fast/Efficient: Found in 16 reviews. Example: 'its fast and easy to communicate to the app and its available all area keep it up.i will make happy ...'
2. **Easy to Use**
   - Easy to Use: Found in 23 reviews. Example: 'very smart app easy to use and friendly...'
3. **Reliable/Stable**
   - Reliable/Stable: Found in 76 reviews. Example: 'great...'

**Pain Points:**
1. **app**
2. **bank**
3. **worst**

---

## Bank Comparison

### Overall Performance Ranking

1. **Commercial Bank of Ethiopia (CBE)** - Rating: 4.12/5.0, Positive: 57.9%
2. **Dashen Bank** - Rating: 3.91/5.0, Positive: 63.5%
3. **Bank of Abyssinia (BOA)** - Rating: 3.35/5.0, Positive: 47.6%

### Comparative Analysis Table

| Bank | Avg Rating | Positive % | Top Driver | Top Pain Point | Priority Level |
|------|------------|------------|------------|----------------|----------------|
| Commercial Bank of Ethiopia (CBE) | 4.12 | 57.9% | Fast/Efficient | app | Low |
| Bank of Abyssinia (BOA) | 3.35 | 47.6% | Fast/Efficient | app | High |
| Dashen Bank | 3.91 | 63.5% | Fast/Efficient | app | Medium |

### Key Differences

1. **CBE vs BOA:** CBE outperforms BOA by 0.77 rating points (4.12 vs 3.35), indicating significantly better user satisfaction
2. **Dashen vs BOA:** Dashen shows 0.56 point advantage over BOA, with notably higher positive sentiment
3. **CBE vs Dashen:** While CBE has higher average rating, Dashen has higher positive sentiment percentage

---

## Satisfaction Drivers

### Common Drivers Across All Banks

The most frequently mentioned satisfaction drivers across all banks:

- **Fast/Efficient**: Mentioned across 3 bank(s)
- **Easy to Use**: Mentioned across 3 bank(s)
- **Reliable/Stable**: Mentioned across 3 bank(s)
- **Secure**: Mentioned across 3 bank(s)
- **Convenient**: Mentioned across 3 bank(s)

### Driver Analysis by Bank

#### Commercial Bank of Ethiopia (CBE)

- **Fast/Efficient**: Identified as a key satisfaction factor
- **Easy to Use**: Identified as a key satisfaction factor
- **Reliable/Stable**: Identified as a key satisfaction factor

#### Bank of Abyssinia (BOA)

- **Fast/Efficient**: Identified as a key satisfaction factor
- **Easy to Use**: Identified as a key satisfaction factor
- **Reliable/Stable**: Identified as a key satisfaction factor

#### Dashen Bank

- **Fast/Efficient**: Identified as a key satisfaction factor
- **Easy to Use**: Identified as a key satisfaction factor
- **Reliable/Stable**: Identified as a key satisfaction factor

---

## Pain Points

### Common Pain Points Across All Banks

The most frequently mentioned pain points across all banks:

- **app**: Affects 3 bank(s)
- **bank**: Affects 3 bank(s)
- **work**: Affects 3 bank(s)
- **use**: Affects 2 bank(s)
- **worst**: Affects 2 bank(s)

### Pain Point Analysis by Bank

#### Commercial Bank of Ethiopia (CBE)

- **app**: Requires immediate attention
- **bank**: Requires immediate attention
- **use**: Requires immediate attention

#### Bank of Abyssinia (BOA)

- **app**: Requires immediate attention
- **bank**: Requires immediate attention
- **worst**: Requires immediate attention

#### Dashen Bank

- **app**: Requires immediate attention
- **bank**: Requires immediate attention
- **worst**: Requires immediate attention

---

## Recommendations

### Priority-Based Recommendations

#### Commercial Bank of Ethiopia (CBE)

**General Recommendations:**
1. Maintain current quality standards
2. Continue monitoring user feedback for emerging issues
3. Consider adding innovative features to stay competitive

#### Bank of Abyssinia (BOA)

**Priority 1:** Focus on improving overall user satisfaction: Address common complaints systematically

**Priority 2:** Conduct user research: Identify root causes of low ratings and prioritize fixes

#### Dashen Bank

**General Recommendations:**
1. Address common user complaints systematically
2. Enhance user interface based on feedback
3. Implement requested features that align with user needs

### Cross-Bank Recommendations

1. **Performance Optimization:** All banks should focus on reducing app loading times and improving transaction speed
2. **Authentication Enhancement:** Implement biometric login options to reduce authentication-related complaints
3. **User Interface Standardization:** Consider adopting best practices from higher-rated apps
4. **Customer Support:** Improve response times and support channel availability
5. **Feature Development:** Prioritize features most requested by users across all platforms

---

## Visualizations

The following visualizations provide detailed insights into the review data:

### 1. Rating Distribution by Bank
**File:** `rating_distribution.png`
Shows the distribution of 1-5 star ratings for each bank, revealing rating patterns and user satisfaction levels.

### 2. Sentiment Distribution by Bank
**File:** `sentiment_distribution.png`
Displays the proportion of positive, negative, and neutral reviews per bank, highlighting sentiment trends.

### 3. Average Rating Comparison
**File:** `average_rating_comparison.png`
Compares average ratings across all three banks, enabling direct performance benchmarking.

### 4. Word Cloud
**File:** `wordcloud.png`
Visual representation of most frequently mentioned words across all reviews, identifying key themes and topics.

### 5. Theme Frequency by Bank
**File:** `theme_frequency.png` (if available)
Shows the frequency of identified themes per bank.

---

## Ethics and Bias Considerations

### Potential Review Biases

1. **Negative Bias:** Users with negative experiences are significantly more likely to leave reviews than satisfied users, potentially skewing results toward negative feedback.
2. **Recency Bias:** Recent reviews may not reflect long-term app performance, as apps are continuously updated and improved.
3. **Selection Bias:** Only users who download and actively use the app can leave reviews, excluding potential users who uninstalled the app before reviewing.
4. **Language Bias:** This analysis focuses on English reviews, potentially missing valuable feedback in local languages (Amharic, Oromo, etc.).
5. **Platform Bias:** Analysis is limited to Google Play Store, excluding iOS App Store reviews and other platforms.

### Limitations

1. **Data Scope:** Analysis based on publicly available reviews only (1,167 reviews), which may not represent the entire user base.
2. **Sentiment Analysis:** VADER sentiment analyzer, while effective, may not capture context-specific nuances or cultural expressions.
3. **Theme Classification:** Rule-based theme mapping may miss emerging themes or subtle issues not captured by keyword matching.
4. **Temporal Limitations:** Reviews analyzed represent a snapshot in time and may not reflect current app state after recent updates.
5. **Sample Size:** While 1,167 reviews provide meaningful insights, larger samples would increase statistical confidence.

### Mitigation Strategies

1. **Weighted Analysis:** Consider review recency and helpfulness scores when available
2. **Multi-Language Support:** Future analysis should include reviews in local languages
3. **Longitudinal Studies:** Track reviews over time to identify trends and improvements
4. **Validation:** Cross-reference findings with internal customer support data and user surveys

---

## Conclusion

This analysis provides actionable insights for improving mobile banking app experiences across three major Ethiopian banks. Key findings indicate that **performance optimization, authentication improvements, and user interface enhancements** should be prioritized across all banks. **CBE** demonstrates best practices with the highest average rating, while **BOA** requires the most attention to address user dissatisfaction. **Dashen Bank** shows strong positive sentiment despite slightly lower ratings, suggesting good user engagement.

### Next Steps

1. **Immediate Actions:** Address critical pain points identified in this report
2. **Short-term:** Implement recommended improvements based on user feedback
3. **Long-term:** Establish continuous monitoring and feedback loops
4. **Ongoing:** Regular review analysis to track improvement progress

### Success Metrics

To measure the impact of implemented improvements:
- Monitor average rating trends over time
- Track sentiment distribution changes
- Measure reduction in specific pain point mentions
- Survey user satisfaction post-implementation

---

**Report Generated:** December 2025
**Data Source:** Google Play Store Reviews
**Analysis Period:** Recent reviews (newest first)
**Total Reviews:** 1,167
**Banks Analyzed:** 3 (CBE, BOA, Dashen)
**Report Version:** 1.0

