import math
from sympy import Matrix
import numpy as np


def eigenvalues_2x2(matrix):
    a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
    trace = a + d
    determinant = a * d - b * c

    # Solve the quadratic equation λ^2 - trace*λ + determinant = 0
    discriminant = trace ** 2 - 4 * determinant
    if discriminant < 0:
        raise ValueError("Matrix has complex eigenvalues.")

    lambda1 = (trace + math.sqrt(discriminant)) / 2
    lambda2 = (trace - math.sqrt(discriminant)) / 2

    return sorted([lambda1, lambda2], reverse=True)


def eigenvalues_2x2_sympy(matrix):
    sympy_matrix = Matrix(matrix)
    eigenvals = sympy_matrix.eigenvals()

    eigenvalues = sorted(eigenvals.keys(), reverse=True)
    return eigenvalues


def eigenvalues_2x2_numpy(matrix):
    np_matrix = np.array(matrix)
    eigenvalues = np.linalg.eigvals(np_matrix)

    return sorted(eigenvalues, reverse=True)


if __name__ == "__main__":
    matrix1 = [[2, 1], [1, 2]]
    matrix2 = [[4, 1], [2, 3]]
    print(eigenvalues_2x2(matrix1))
    print(eigenvalues_2x2(matrix2))

    print(eigenvalues_2x2_sympy(matrix1))
    print(eigenvalues_2x2_numpy(matrix2))
