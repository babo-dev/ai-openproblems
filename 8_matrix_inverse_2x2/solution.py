from __future__ import annotations


def inverse_2x2(matrix: list[list[float]]) -> [list[list[float]] | None]:
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if det == 0:
        return None

    delim = 1 / det

    inverse = [[matrix[1][1]*delim, -matrix[0][1]*delim],  [-matrix[1][0]*delim, matrix[0][0]*delim]]
    return inverse


if __name__ == "__main__":
    matrix = [[4, 7], [2, 6]]
    inverse = inverse_2x2(matrix)
    if inverse is not None:
        print(f"The inverse of the matrix is: {inverse}")
    else:
        print("The matrix is singular and does not have an inverse.")
