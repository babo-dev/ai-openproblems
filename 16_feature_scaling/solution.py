import numpy as np


def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
    # Standardization - z-score normalization: (x - mean) / std_dev
    mean = np.mean(data, axis=0)  # mean for each feature
    std_dev = np.std(data, axis=0)  # standard deviation for each feature
    standardized_data = (data - mean) / std_dev
    standardized_data = np.round(standardized_data, 4)

    # Min-Max Normalization: (x - min) / (max - min)
    min_vals = np.min(data, axis=0)  # minimum for each feature
    max_vals = np.max(data, axis=0)  # maximum for each feature
    normalized_data = (data - min_vals) / (max_vals - min_vals)
    normalized_data = np.round(normalized_data, 4)

    return standardized_data, normalized_data


if __name__ == "__main__":
    data = np.array([
        [10, 20],
        [20, 30],
        [30, 40]
    ])
    standardized, normalized = feature_scaling(data)
    print("Standardized Data: ", standardized)
    print("Normalized Data: ", normalized)
