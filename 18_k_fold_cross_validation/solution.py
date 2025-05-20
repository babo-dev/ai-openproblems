import numpy as np


def k_fold_cross_validation(X, y, k=5, shuffle=False):
    n = len(X)
    indices = np.arange(n)

    if shuffle:
        np.random.shuffle(indices)

    splits = []

    fold_size = n // k

    for i in range(k):
        test_start = i * fold_size
        test_end = (i + 1) * fold_size if i != k - 1 else n
        test_indices = indices[test_start:test_end]

        train_indices = np.concatenate((indices[:test_start], indices[test_end:]))

        splits.append((train_indices.tolist(), test_indices.tolist()))

    return splits


if __name__ == "__main__":
    X = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    y = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    splits = k_fold_cross_validation(X, y, k=5, shuffle=False)
    print(splits)

    splits_shuffled = k_fold_cross_validation(X, y, k=5, shuffle=True)
    print(splits_shuffled)
