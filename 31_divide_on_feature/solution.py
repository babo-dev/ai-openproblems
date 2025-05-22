import numpy as np


def divide_on_feature(X, feature_i, threshold):
    output = []
    include = X[X[:, feature_i] >= threshold]
    not_include = X[X[:, feature_i] < threshold]

    output.append(include)
    output.append(not_include)

    return output


if __name__ == "__main__":
    X = np.array([[1, 2],
                  [3, 4],
                  [5, 6],
                  [7, 8],
                  [9, 10]])
    feature_i = 0
    threshold = 5

    print(divide_on_feature(X, feature_i, threshold))
