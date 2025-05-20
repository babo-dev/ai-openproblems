import math


def sigmoid(x):
    result = 1 / (1 + math.exp(-x))
    return round(result, 4)


if __name__ == "__main__":
    print(sigmoid(1))
