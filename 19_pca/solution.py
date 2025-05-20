import numpy as np


def pca(data, k):
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    standardized_data = (data - mean) / std

    covariance_matrix = np.cov(standardized_data, rowvar=False)

    eigenvalues, eigenvectors = np.linalg.eigh(covariance_matrix)

    sorted_indices = np.argsort(eigenvalues)[::-1]
    sorted_eigenvectors = eigenvectors[:, sorted_indices]

    top_k_eigenvectors = sorted_eigenvectors[:, :k]

    transformed_data = np.dot(standardized_data, top_k_eigenvectors)

    return top_k_eigenvectors, transformed_data


if __name__ == "__main__":
    # data = np.array([
    #     [2.5, 2.4],
    #     [0.5, 0.7],
    #     [2.2, 2.9],
    #     [1.9, 2.2],
    #     [3.1, 3.0],
    #     [2.3, 2.7],
    #     [2.0, 1.6],
    #     [1.0, 1.1],
    #     [1.5, 1.6],
    #     [1.1, 0.9]
    # ])

    data = np.array([[4, 2, 1], [5, 6, 7], [9, 12, 1], [4, 6, 7]])
    k = 2
    principal_components, transformed_data = pca(data, k)

    print("Principal Components:")
    print(principal_components)
    print("\nTransformed Data:")
    print(transformed_data)
