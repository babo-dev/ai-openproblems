import math


def softmax(scores):
    # maximum value in x for numerical stability
    max_x = max(scores)

    # exponential and sum them
    exp_x = [math.exp(i - max_x) for i in scores]
    sum_exp_x = sum(exp_x)

    softmax_values = [round(i / sum_exp_x, 4) for i in exp_x]

    return softmax_values


if __name__ == "__main__":
    x = [1.0, 2.0, 3.0]
    print(softmax(x))