import numpy as np


def get_random_subsets(X, y, n_subsets, replacements=True, seed=42):
    np.random.seed(seed)
    n_samples = X.shape[0]
    subsets = []

    for _ in range(n_subsets):
        if replacements:
            indices = np.random.choice(n_samples, size=n_samples, replace=True)
        else:
            subset_size = n_samples // 2
            indices = np.random.choice(n_samples, size=subset_size, replace=False)

        X_subset = X[indices]
        y_subset = y[indices]

        subsets.append((X_subset, y_subset))
    return subsets


if __name__ == "__main__":
    # X = np.array([[1, 2],
    #               [3, 4],
    #               [5, 6],
    #               [7, 8],
    #               [9, 10]])
    # y = np.array([1, 2, 3, 4, 5])
    # n_subsets = 3
    # replacements = False

    X = np.array([[1, 1], [2, 2], [3, 3], [4, 4]])
    y = np.array([10, 20, 30, 40])
    print(get_random_subsets(X, y, 1, True, seed=42))
