# Phishing Email Detection

A starter machine-learning project for detecting phishing emails from text and metadata features.

## Project Structure

- data/: raw, processed, and external datasets
- notebooks/: exploratory and modeling notebooks
- src/: reusable data loading, feature engineering, modeling, and pipeline modules
- api/: FastAPI application for serving predictions
- tests/: unit tests for core components

## Quick Start

1. Create a virtual environment
2. Install dependencies: `pip install -r requirements.txt`
3. Run training: `python scripts/run_training.py`
4. Start API: `uvicorn api.app:app --reload`
