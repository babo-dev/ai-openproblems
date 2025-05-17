from __future__ import annotations


def matrixmul(a: list[list[int | float]],
              b: list[list[int | float]]) -> [list[list[int | float]] | int]:
    if len(a[0]) != len(b):
        return -1

    rows_a, cols_a = len(a), len(a[0])
    rows_b, cols_b = len(b), len(b[0])
    C = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                C[i][j] += a[i][k] * b[k][j]

    return C


if __name__ == "__main__":
    a = [[1, 2, 3], [4, 5, 6]]
    b = [[7, 8], [9, 10], [11, 12]]
    print(matrixmul(a, b))  # Output: -1

    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]
    print(matrixmul(a, b))  # Output: [[19, 22], [43, 50]]

    a = []
    b = [[1, 2], [3, 4]]
    print(matrixmul(a, b))  # Output: -1

    a = [[1, 2], [3, 4]]
    b = []
    print(matrixmul(a, b))  # Output: -1

    a = [[1]]
    b = [[1]]
    print(matrixmul(a, b))  # Output: [[1]]
