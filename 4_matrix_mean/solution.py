def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    means = []
    if mode == "row":
        for row in matrix:
            means.append(sum(row) / len(row))
    elif mode == "column":
        for row in matrix:
            for c_ind in range(len(row)):
                if len(means) <= c_ind:
                    means.append(row[c_ind])
                else:
                    means[c_ind] += row[c_ind]
        for i in range(len(means)):
            means[i] /= len(matrix)
    else:
        print("unknown mode")

    return means

if __name__ == "__main__":
    m = [[1,2,3,5], [6,7,8,9]]
    #means = calculate_matrix_mean(m, "row")
    means = calculate_matrix_mean(m, "column")
    print(f"matrix: {m}")
    print(means)

