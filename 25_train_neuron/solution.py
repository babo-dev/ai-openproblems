import numpy as np


def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float,
                 learning_rate: float, epochs: int) -> (list[float], float, list[float]):
    mse_values = []
    weights = np.array(initial_weights, dtype=float)
    bias = initial_bias

    for epoch in range(epochs):
        z = features @ weights + bias
        predictions = 1 / (1 + np.exp(-z))

        mse = np.mean((predictions - labels) ** 2)
        mse_values.append(round(mse, 4))

        errors = predictions - labels
        gradient_weights = np.dot(features.T, errors) / len(labels)
        gradient_bias = np.mean(errors)

        weights -= learning_rate * gradient_weights
        bias -= learning_rate * gradient_bias

    weights = np.round(weights, 4).tolist()
    bias = round(bias, 4)

    return weights, bias, mse_values


if __name__ == "__main__":
    features = np.array([[1.0, 2.0], [2.0, 1.0], [-1.0, -2.0]])
    labels = np.array([1, 0, 0])
    weights = np.array([0.1, -0.2])
    bias = 0.0

    updated_weights, updated_bias, mse_values = train_neuron(features, labels, weights, bias, 0.1, 2)
    print("Updated Weights:", updated_weights)
    print("Updated Bias:", updated_bias)
    print("MSE Values:", mse_values)