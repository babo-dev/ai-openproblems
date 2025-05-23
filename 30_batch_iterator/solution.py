import numpy as np


def batch_iterator(X, y=None, batch_size=64):
    output = []
    for i in range(0, len(X), batch_size):
        if y is not None:
            batch = [X[i:i + batch_size].tolist(), y[i:i + batch_size].tolist()]
        else:
            batch = X[i:i + batch_size].tolist()
        output.append(batch)

    return output


if __name__ == "__main__":
    X = np.array([[1, 2],
                  [3, 4],
                  [5, 6],
                  [7, 8],
                  [9, 10]])
    y = np.array([1, 2, 3, 4, 5])
    batch_size = 2

    batches = batch_iterator(X, y, batch_size)
    print(batches)

