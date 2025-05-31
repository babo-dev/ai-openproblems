import numpy as np


def layer_normalization(X: np.ndarray, gamma: np.ndarray, beta: np.ndarray, epsilon: float = 1e-5) -> np.ndarray:
    """
    Parameters:
        X : Input tensor of shape (batch_size, sequence_length, d_model).
        gamma : Scaling parameter of shape (1, 1, d_model).
        beta : Shifting parameter of shape (1, 1, d_model).
        epsilon : Small value to avoid division by zero.

    Returns:
        numpy.ndarray: Normalized tensor of the same shape as X.
    """
    mean = np.mean(X, axis=-1, keepdims=True)  # Shape: (batch_size, sequence_length, 1)
    variance = np.var(X, axis=-1, keepdims=True)  # Shape: (batch_size, sequence_length, 1)

    normalized_X = (X - mean) / np.sqrt(variance + epsilon)

    output = gamma * normalized_X + beta

    return output


if __name__ == "__main__":
    np.random.seed(42)
    # X = np.random.randn(2, 2, 3)
    # X = np.array([[[1000]], [[2000]], [[3000]]])
    X = np.array([[[1, 1, 5]]])
    gamma = np.ones(3).reshape(1, 1, -1)
    beta = np.zeros(3).reshape(1, 1, -1)
    print(layer_normalization(X, gamma, beta))
