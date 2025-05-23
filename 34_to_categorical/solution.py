import numpy as np


def to_categorical(x, n_col=None):
    if n_col is None:
        n_col = np.max(x) + 1

    one_hot = np.zeros((x.size, n_col), dtype=np.float32)
    one_hot[np.arange(x.size), x] = 1

    return one_hot


if __name__ == "__main__":
    x = np.array([0, 1, 2, 1, 0])
    output = to_categorical(x)
    print(output)
