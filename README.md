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

## Architecture

                    Predicted
                 Phishing    Safe
    Actual  Phishing   2345      112
            Safe        98     2445

    True Positives (TP): 2345
    True Negatives (TN): 2445
    False Positives (FP): 98
    False Negatives (FN): 112
    ┌─────────────────────────────────────────────────────────────────────┐
│                        USER INTERFACE LAYER                       │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐       │
│  │ Web Interface │    │  REST API    │    │ CLI Tool     │       │
│  └──────────────┘    └──────────────┘    └──────────────┘       │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│                      APPLICATION LAYER                            │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │           Prediction Pipeline                            │    │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐  │    │
│  │  │Input    │→│Feature  │→│Model   │→│Result   │  │    │
│  │  │Parser   │  │Extractor│  │Predictor│  │Formatter│  │    │
│  │  └─────────┘  └─────────┘  └─────────┘  └─────────┘  │    │
│  └──────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│                       MODEL LAYER                                  │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │              Trained Models                              │    │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐ │    │
│  │  │ Random Forest│  │ Logistic     │  │ XGBoost      │ │    │
│  │  │ (Best Model) │  │ Regression   │  │ Classifier   │ │    │
│  │  └──────────────┘  └──────────────┘  └──────────────┘ │    │
│  └──────────────────────────────────────────────────────────┘    │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │           Vectorizers & Transformers                     │    │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐ │    │
│  │  │  TF-IDF      │  │  Count       │  │  Label       │ │    │
│  │  │  Vectorizer  │  │  Vectorizer  │  │  Encoder     │ │    │
│  │  └──────────────┘  └──────────────┘  └──────────────┘ │    │
│  └──────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│                      DATA LAYER                                    │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐       │
│  │  Raw Data    │    │  Processed   │    │  Feature     │       │
│  │  (CSV/JSON)  │→   │  Data        │→   │  Store       │       │
│  └──────────────┘    └──────────────┘    └──────────────┘       │
└─────────────────────────────────────────────────────────────────────┘
