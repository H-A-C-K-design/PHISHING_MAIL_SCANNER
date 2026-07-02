from src.models.model_predictor import predict


def test_predict_uses_model_output():
    class DummyModel:
        def predict(self, features):
            return [1]

    assert predict(DummyModel(), [[0, 0]]) == [1]
from src.models.model_predictor import predict


def test_predict_returns_array():
    class DummyModel:
        def predict(self, features):
            return [0]

    result = predict(DummyModel(), [[0, 0, 0, 0, 0]])
    assert result == [0]
