import numpy as np


def random_shuffle(X, y, seed=None):
    if seed is not None:
        np.random.seed(seed)

    indices = np.arange(len(X))
    np.random.shuffle(indices)

    X_shuffled = X[indices]
    y_shuffled = y[indices]

    return X_shuffled, y_shuffled


if __name__ == "__main__":
    X = np.array([[1, 2],
                  [3, 4],
                  [5, 6],
                  [7, 8]])
    y = np.array([1, 2, 3, 4])

    X_shuffled, y_shuffled = random_shuffle(X, y, seed=42)

    print(X_shuffled)
    print(y_shuffled)