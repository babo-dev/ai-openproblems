import math


def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> \
        (list[float], float):
    predictions = []
    for i in range(len(features)):
        prediction = 0
        for j in range(len(features[i])):
            prediction += features[i][j] * weights[j]
        prediction += bias
        predictions.append(prediction)

    for i in range(len(predictions)):
        predictions[i] = round(1 / (1 + math.exp(-predictions[i])), 4)

    loss = 0
    for i in range(len(predictions)):
        loss += (labels[i] - predictions[i]) ** 2
    loss /= len(predictions)

    return predictions, round(loss, 4)


if __name__ == "__main__":
    features = [[0.5, 1.0], [-1.5, -2.0], [2.0, 1.5]]
    labels = [0, 1, 0]
    weights = [0.7, -0.4]
    bias = -0.1

    predictions, loss = single_neuron_model(features, labels, weights, bias)
    print("Predictions:", predictions)
    print("Loss:", loss)
