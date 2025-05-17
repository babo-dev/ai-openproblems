import numpy as np


def solve_jacobi(A: np.ndarray, b: np.ndarray, n_iterations: int = 10) -> list:
    n = len(b)

    x = np.zeros(n)

    for _ in range(n_iterations):
        x_new = np.zeros(n)
        for i in range(n):
            sigma = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sigma) / A[i][i]

        x = np.round(x_new, 4)

    return x.tolist()


# Test cases
if __name__ == "__main__":
    A1 = np.array([[5, -2, 3], [-3, 9, 1], [2, -1, -7]])
    b1 = np.array([-1, 2, 3])
    print(solve_jacobi(A1, b1, n_iterations=2))

    A2 = np.array([[10, -1, 2], [-1, 11, -1], [2, -1, 10]])
    b2 = np.array([6, 25, -11])
    print(solve_jacobi(A2, b2, n_iterations=10))