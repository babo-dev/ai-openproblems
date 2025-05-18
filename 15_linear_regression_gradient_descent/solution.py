import numpy as np


def linear_regression_gradient_descent(X, y, alpha, num_iterations):
    theta = np.zeros(X.shape[1])

    m = len(y)

    for _ in range(num_iterations):
        predictions = X @ theta
        errors = predictions - y

        gradient = (1 / m) * (X.T @ errors)

        theta -= alpha * gradient

    theta_rounded = np.round(theta, 4)

    return theta_rounded


if __name__ == "__main__":
    X1 = np.array([[1, 1], [1, 2], [1, 3], [1, 4]])
    y1 = np.array([2, 4, 6, 8])
    alpha1 = 0.01
    num_iterations1 = 1000
    print(linear_regression_gradient_descent(X1, y1, alpha1, num_iterations1))

    X2 = np.array([[1, 1, 2], [1, 2, 3], [1, 4, 5], [1, 3, 1]])
    y2 = np.array([3, 5, 9, 4])
    alpha2 = 0.01
    num_iterations2 = 1000
    print(linear_regression_gradient_descent(X2, y2, alpha2, num_iterations2))