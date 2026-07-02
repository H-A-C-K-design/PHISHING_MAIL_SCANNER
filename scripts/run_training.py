from pathlib import Path
import sys

# Ensure project root is on sys.path so `src` package imports work when running
# this script directly (python scripts/run_training.py)
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.pipeline.training_pipeline import run_training


if __name__ == "__main__":
    data_path = Path("data/raw/combined_dataset.csv")
    if not data_path.exists():
        print("Dataset not found. Add a CSV file to data/raw/combined_dataset.csv")
    else:
        model, _, _ = run_training(str(data_path))
        print("Training completed.", model)
