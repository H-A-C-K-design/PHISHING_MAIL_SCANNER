from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.models.model_predictor import predict


if __name__ == "__main__":
    sample_features = [[1, 3, 120, 20, 1]]
    print(predict(None, sample_features))
