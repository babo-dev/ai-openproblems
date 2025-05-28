import numpy as np


def simple_conv2d(input_matrix, kernel, padding=0, stride=1):
    input_height, input_width = input_matrix.shape
    kernel_height, kernel_width = kernel.shape

    output_height = (input_height + 2 * padding - kernel_height) // stride + 1
    output_width = (input_width + 2 * padding - kernel_width) // stride + 1

    output_matrix = np.zeros((output_height, output_width))

    padded_input = np.pad(input_matrix, pad_width=padding, mode='constant', constant_values=0)

    for i in range(0, output_height):
        for j in range(0, output_width):
            row_start = i * stride
            row_end = row_start + kernel_height
            col_start = j * stride
            col_end = col_start + kernel_width

            region = padded_input[row_start:row_end, col_start:col_end]

            output_matrix[i, j] = np.sum(region * kernel)

    return output_matrix


if __name__ == "__main__":
    input_matrix = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ])

    kernel = np.array([
        [1, 0],
        [-1, 1]
    ])

    padding = 1
    stride = 2

    output = simple_conv2d(input_matrix, kernel, padding, stride)
    print(output)
