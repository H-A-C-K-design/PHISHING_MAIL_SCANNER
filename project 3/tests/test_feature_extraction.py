import pandas as pd
from src.features.feature_extractor import extract_features


def test_extract_features_returns_expected_columns():
    df = pd.DataFrame({
        "content": ["Urgent! Click here to verify your password"],
        "subject": ["Invoice"],
    })
    features = extract_features(df)
    assert list(features.columns) == ["contains_url", "keyword_count", "char_count", "word_count", "has_subject"]
    assert features.iloc[0]["keyword_count"] >= 1
