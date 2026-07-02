import pandas as pd
from .keyword_features import keyword_count
from .textual_features import char_count, word_count
from .url_features import contains_url
from .header_features import has_subject


def extract_features(df: pd.DataFrame) -> pd.DataFrame:
    features = pd.DataFrame()
    features["contains_url"] = df["content"].apply(contains_url) if "content" in df.columns else []
    features["keyword_count"] = df["content"].apply(keyword_count) if "content" in df.columns else []
    features["char_count"] = df["content"].apply(char_count) if "content" in df.columns else []
    features["word_count"] = df["content"].apply(word_count) if "content" in df.columns else []
    features["has_subject"] = df["subject"].apply(has_subject) if "subject" in df.columns else []
    return features
