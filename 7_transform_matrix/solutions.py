from __future__ import annotations

import numpy as np


def transform_matrix(A: list[list[int | float]], T: list[list[int | float]], S: list[list[int | float]]) -> list[
    list[int | float]
]:
    T = np.array(T)
    S = np.array(S)
    A = np.array(A)
    if T.shape[0] != T.shape[1] or S.shape[0] != S.shape[1]:
        return -1

    if np.linalg.det(T) == 0 or np.linalg.det(S) == 0:
        return -1

    # Compute the inverse of T
    T_inv = np.linalg.inv(T)

    # Perform the transformation: T_inv @ A @ S
    result = T_inv @ A @ S

    return result.tolist()


if __name__ == "__main__":
    A = [[1, 2], [3, 4]]
    T = [[1, 0], [0, 1]]
    S = [[2, 0], [0, 2]]

    print(transform_matrix(A, T, S))
