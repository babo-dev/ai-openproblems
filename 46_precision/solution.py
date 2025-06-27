import numpy as np


def precision(y_true: np.ndarray, y_pred: np.ndarray):
    true_positive = np.sum((y_true == 1) & (y_pred == 1))
    false_positive = np.sum((y_true == 0) & (y_pred == 1))

    if true_positive + false_positive == 0:
        return 0.0

    return true_positive / (true_positive + false_positive)


if __name__ == "__main__":
    y_true = np.array([1, 0, 1, 1, 0, 1, 0])
    y_pred = np.array([1, 0, 1, 0, 0, 1, 1])
    print(precision(y_true, y_pred))
