from sklearn.model_selection import train_test_split
import math


def split_data(X, y, test_size=0.2, random_state=42):
    n_samples = len(y)
    n_classes = len(set(y)) if n_samples > 0 else 0

    # Compute the absolute number of test samples
    n_test = math.ceil(n_samples * test_size)

    # If there are too few test samples to stratify across classes, skip stratify
    stratify = y if n_test >= n_classes and n_classes > 1 else None

    return train_test_split(X, y, test_size=test_size, random_state=random_state, stratify=stratify)
