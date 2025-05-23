import numpy as np


def accuracy_score(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    # np.mean(y_true == y_pred)
    return np.sum(y_true == y_pred) / len(y_true)


if __name__ == "__main__":
    y_true = np.array([1, 0, 1, 1, 0, 1])
    y_pred = np.array([1, 0, 0, 1, 0, 1])
    output = accuracy_score(y_true, y_pred)
    print(output)
