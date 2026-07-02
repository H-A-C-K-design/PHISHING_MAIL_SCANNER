import numpy as np
from sklearn.linear_model import LogisticRegression
from src.models.model_trainer import train_logistic_regression


def test_train_logistic_regression_returns_model():
    X_train = np.array([[0, 0], [1, 1], [0, 1], [1, 0]])
    y_train = np.array([0, 1, 1, 0])
    model = train_logistic_regression(X_train, y_train)
    assert isinstance(model, LogisticRegression)
