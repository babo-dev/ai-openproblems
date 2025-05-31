import numpy as np
import copy
import math

# DO NOT CHANGE SEED
np.random.seed(42)


# DO NOT CHANGE LAYER CLASS
class Layer(object):

    def set_input_shape(self, shape):
        self.input_shape = shape

    def layer_name(self):
        return self.__class__.__name__

    def parameters(self):
        return 0

    def forward_pass(self, X, training):
        raise NotImplementedError()

    def backward_pass(self, accum_grad):
        raise NotImplementedError()

    def output_shape(self):
        raise NotImplementedError()


class Dense(Layer):
    def __init__(self, n_units, input_shape=None):
        self.layer_input = None
        self.input_shape = input_shape
        self.n_units = n_units
        self.trainable = True
        self.W = None
        self.w0 = None
        self.optimizer_W = None
        self.optimizer_w0 = None

    def initialize(self, optimizer):
        # Initialize weights W using a uniform distribution with limit 1 / sqrt(input_shape[0])
        limit = 1 / np.sqrt(self.input_shape[0])
        self.W = np.random.uniform(-limit, limit, (self.input_shape[0], self.n_units))
        self.w0 = np.zeros((1, self.n_units))
        self.optimizer_W = optimizer
        self.optimizer_w0 = optimizer

    @property
    def parameters(self):
        return self.W.size + self.w0.size

    def forward_pass(self, X, training=True):
        self.X = X  # Store input for backward pass
        return np.dot(X, self.W) + self.w0

    def backward_pass(self, accum_grad):
        # Calculate gradient with respect to input: dY/dX = accum_grad * W.T
        grad_input = np.dot(accum_grad, self.W.T)

        if self.trainable:
            # Calculate gradients with respect to weights and biases
            grad_W = np.dot(self.X.T, accum_grad)
            grad_w0 = np.sum(accum_grad, axis=0, keepdims=True)

            # Update weights and biases using the optimizer's update rule
            self.W = self.optimizer_W.update(self.W, grad_W)
            self.w0 = self.optimizer_w0.update(self.w0, grad_w0)

        return grad_input

    def number_of_parameters(self):
        return (self.n_units, )


if __name__ == "__main__":
    # Initialize a Dense layer with 3 neurons and input shape (2,)
    dense_layer = Dense(n_units=3, input_shape=(2,))


    class MockOptimizer:
        def update(self, weights, grad):
            return weights - 0.01 * grad


    optimizer = MockOptimizer()

    # Initialize the Dense layer with the mock optimizer
    dense_layer.initialize(optimizer)

    # Perform a forward pass with sample input data
    X = np.array([[1, 2]])
    output = dense_layer.forward_pass(X)
    print("Forward pass output:", output)

    # Perform a backward pass with sample gradient
    accum_grad = np.array([[0.1, 0.2, 0.3]])
    back_output = dense_layer.backward_pass(accum_grad)
    print("Backward pass output:", back_output)
