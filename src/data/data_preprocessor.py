import pandas as pd


def clean_text(series: pd.Series) -> pd.Series:
    return series.fillna("").astype(str).str.strip().str.lower()
