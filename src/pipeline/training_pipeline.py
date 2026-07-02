from src.data.data_loader import load_csv
from src.data.data_preprocessor import clean_text
from src.data.data_splitter import split_data
from src.features.feature_extractor import extract_features
from src.models.model_trainer import train_logistic_regression


def run_training(data_path: str):
    df = load_csv(data_path)
    df["content"] = clean_text(df["content"])
    df["subject"] = clean_text(df["subject"])

    X = extract_features(df)
    y = df["label"]
    X_train, X_test, y_train, y_test = split_data(X, y)

    model = train_logistic_regression(X_train, y_train)
    return model, X_test, y_test
