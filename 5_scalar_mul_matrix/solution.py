def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    for row in matrix:
        for ind in range(len(row)):
            row[ind] *= scalar
    return matrix

if __name__ == "__main__":
    a = [[1,2,3,4], [5,6,7,8]]
    print(a)
    print(scalar_multiply(a, 3))
