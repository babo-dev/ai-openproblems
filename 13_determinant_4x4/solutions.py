def determinant_4x4(matrix):
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for col in range(len(matrix)):
        # cofactor sign (-1)^(row + col)
        sign = (-1) ** col

        minor = [row[:col] + row[col + 1:] for row in matrix[1:]]

        # Recursively compute the determinant of the minor matrix
        minor_det = determinant_4x4(minor)

        det += sign * matrix[0][col] * minor_det

    return det


if __name__ == "__main__":
    A1 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    print(determinant_4x4(A1))
    A2 = [
        [1, 0, 0, 0],
        [0, 2, 0, 0],
        [0, 0, 3, 0],
        [0, 0, 0, 4]
    ]
    print(determinant_4x4(A2))