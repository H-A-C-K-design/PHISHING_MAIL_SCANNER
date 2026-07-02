from src.features.feature_extractor import extract_features


def build_feature_frame(df):
    return extract_features(df)
