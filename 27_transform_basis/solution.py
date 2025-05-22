import numpy as np


def transformation_matrix(B, C):
    B = np.array(B)
    C = np.array(C)

    C_inv = np.linalg.inv(C)

    # P = C_inv * B
    P = np.dot(C_inv, B)

    return P


if __name__ == "__main__":
    B = [[1, 0, 0],
         [0, 1, 0],
         [0, 0, 1]]

    C = [[1, 2.3, 3],
         [4.4, 25, 6],
         [7.4, 8, 9]]

    P = transformation_matrix(B, C)
    print(P)