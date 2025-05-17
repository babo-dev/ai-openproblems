import numpy as np


def linear_regression_normal_equation(X, y):
    X = np.array(X)
    y = np.array(y)

    # theta = (X^T X)^(-1) X^T y
    theta = np.linalg.inv(X.T @ X) @ X.T @ y

    theta_rounded = np.round(theta, 4)

    return theta_rounded.tolist()


if __name__ == "__main__":
    X1 = [[1], [2], [3], [4]]
    y1 = [2, 4, 6, 8]
    print(linear_regression_normal_equation(X1, y1))

    X2 = [[1, 1], [1, 2], [1, 3]]
    y2 = [1, 2, 3]
    print(linear_regression_normal_equation(X2, y2))