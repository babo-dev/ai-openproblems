import numpy as np


def calculate_correlation_matrix(X, Y=None):
    if Y is None:
        Y = X
    # Standardize X and Y by subtracting their means and dividing by their standard deviations
    X_standardized = (X - np.mean(X, axis=0)) / np.std(X, axis=0)
    Y_standardized = (Y - np.mean(Y, axis=0)) / np.std(Y, axis=0)

    # Compute the correlation matrix using matrix multiplication
    correlation_matrix = np.dot(X_standardized.T, Y_standardized) / X.shape[0]

    return correlation_matrix


if __name__ == "__main__":
    X = np.array([[1, 2], [3, 4], [5, 6]])
    # Y = np.array([[7, 8], [9, 10], [11, 12]])
    correlation_matrix = calculate_correlation_matrix(X)
    print("Correlation matrix:\n", correlation_matrix)
