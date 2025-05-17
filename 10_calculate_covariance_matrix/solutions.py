import numpy as np


def covariance_matrix_numpy(data):
    data = np.array(data)
    cov_matrix = np.cov(data)

    return cov_matrix.tolist()


def covariance_matrix(vectors: list[list[float]]):
    n_features = len(vectors)
    n_observations = len(vectors[0])  # observations

    means = [sum(feature) / n_observations for feature in vectors]  # mean of each feature

    centered_data = [[x - mean for x in feature] for feature, mean in zip(vectors, means)]

    covariance_matrix = []
    for i in range(n_features):
        row = []
        for j in range(n_features):
            cov = sum(centered_data[i][k] * centered_data[j][k] for k in range(n_observations)) / (n_observations - 1)
            row.append(cov)
        covariance_matrix.append(row)

    return covariance_matrix


if __name__ == "__main__":
    func = covariance_matrix
    data1 = [
        [1, 2, 3],  # Feature 1
        [4, 5, 6]  # Feature 2
    ]
    print(func(data1))

    data2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    print(func(data2))