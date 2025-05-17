from __future__ import annotations


def transpose_matrix(matrix: list[list[int | float]]) -> list[list[int | float]]:
    res = []
    for ind in range(len(matrix)):
        for numb_ind in range(len(matrix[ind])):
            if ind == 0:
                res.append([matrix[ind][numb_ind]])
            else:
                res[numb_ind].append(matrix[ind][numb_ind])
    return res


if __name__ == "__main__":
    m = [[1, 2, 3, 4], [5, 6, 7, 8]]
    print(f"original: {m}")
    print(transpose_matrix(m))
