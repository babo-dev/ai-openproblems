Single Neuron

Write a Python function that simulates a single neuron with a sigmoid activation function for 
binary classification, handling multidimensional input features. The function should take a 
list of feature vectors (each vector representing multiple features for an example), 
associated true binary labels, and the neuron's weights (one for each feature) and bias as input. 
It should return the predicted probabilities after sigmoid activation and the mean squared error 
between the predicted probabilities and the true labels, both rounded to four decimal places.

**Example:**

Input:
```python
features = [[0.5, 1.0], [-1.5, -2.0], [2.0, 1.5]], labels = [0, 1, 0], weights = [0.7, -0.4], bias = -0.1
```

Output:

([0.4626, 0.4134, 0.6682], 0.3349)

Reasoning:

For each input vector, the weighted sum is calculated by multiplying each feature by its corresponding weight,
adding these up along with the bias, then applying the sigmoid function to produce a probability. 
The MSE is calculated as the average squared difference between each predicted probability and 
the corresponding true label.