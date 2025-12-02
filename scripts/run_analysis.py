#!/usr/bin/env python3
"""
Run sentiment annotation on cleaned reviews
"""

import logging
import os
import pandas as pd

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.fintech_app_reviews.config import load_config
from src.fintech_app_reviews.nlp.sentiment import annotate_dataframe

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

def run_sentiment(config_path="configs/nlp.yaml",
                  input_csv=None,
                  output_csv="data/processed/reviews_with_sentiment.csv"):
    # Auto-detect input file if not provided
    if input_csv is None:
        possible_inputs = [
            "data/processed/reviews.csv",
            "data/interim/interim_reviews.csv",
            "data/interim/cleaned_reviews.csv",
            "data/raw/raw_reviews.csv"
        ]
        for path in possible_inputs:
            if os.path.exists(path):
                input_csv = path
                logger.info(f"Auto-detected input file: {input_csv}")
                break
        if input_csv is None:
            logger.error("No input CSV found. Please provide input_csv parameter or ensure data files exist.")
            return
    
    cfg = load_config(config_path) if os.path.exists(config_path) else {}
    engine_cfg = cfg.get("nlp", {}).get("sentiment", {}) if cfg else {}
    engine_preference = ["transformer", "vader"] if engine_cfg.get("engine", "vader") == "transformer" else ["vader"]

    if not os.path.exists(input_csv):
        logger.error("Input CSV not found: %s", input_csv)
        return

    try:
        df = pd.read_csv(input_csv)
        logger.info("Loaded %d reviews", len(df))
    except Exception as e:
        logger.exception("Failed to load CSV: %s", e)
        return

    try:
        # Map column name if needed
        text_col = "review_text" if "review_text" in df.columns else "review"
        df = annotate_dataframe(df, text_col=text_col)
        logger.info("Sentiment annotation complete")
    except Exception as e:
        logger.exception("Sentiment annotation failed: %s", e)
        return

    os.makedirs(os.path.dirname(output_csv), exist_ok=True)
    try:
        df.to_csv(output_csv, index=False)
        logger.info("Saved sentiment CSV: %s", output_csv)
    except Exception as e:
        logger.exception("Failed to save CSV: %s", e)


if __name__ == "__main__":
    run_sentiment()
