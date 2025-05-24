import numpy as np


def log_softmax(A):
    A_max = np.max(A)
    log_sum_exp = np.log(np.sum(np.exp(A - A_max)))

    return A - A_max - log_sum_exp


# Real world example
def cross_entropy_loss(logits, true_class):
    log_probs = log_softmax(logits)

    # log-probability of the true class
    return -log_probs[true_class]


if __name__ == "__main__":
    A = np.array([1.0, 2.0, 3.0])
    loss =  cross_entropy_loss(A, 1)
    print(loss)
