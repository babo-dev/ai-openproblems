import numpy as np


def make_diagonal(x: np.ndarray) -> np.ndarray:
    output = np.zeros((x.size, x.size), dtype=x.dtype)

    for i in range(x.size):
        output[i, i] = x[i]

    return output


if __name__ == "__main__":
    x = np.array([1, 2, 3])
    print(make_diagonal(x))
