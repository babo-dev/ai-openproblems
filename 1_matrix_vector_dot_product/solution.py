from __future__ import annotations


def matrix_dot_vector(matrix: list[list[int | float]], vector: list[int | float]) -> int | list[int]:
    if len(matrix[-1]) != len(vector):
        return -1
    c = []
    for m_small in matrix:
        res = 0
        for i in range(len(m_small)):
            res += m_small[i] * vector[i]
        c.append(res)
    return c


if __name__ == "__main__":
    a = [[1, 2, 3], [4, 5, 6]]
    b = [7, 8, 9]
    print(matrix_dot_vector(a, b))
