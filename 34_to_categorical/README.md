### One-Hot Encoding of Nominal Values

Write a Python function to perform one-hot encoding of nominal values. The function should take 
in a 1D numpy array x of integer values and an optional integer n_col representing the number 
of columns for the one-hot encoded array. If n_col is not provided, it should be automatically 
determined from the input array.

**Example:**

Input:
```python
x = np.array([0, 1, 2, 1, 0])
output = to_categorical(x)
print(output)
```

Output:
```
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]
#  [0. 1. 0.]
#  [1. 0. 0.]]
```
Reasoning:

Each element in the input array is transformed into a one-hot encoded vector, where the index 
corresponding to the value in the input array is set to 1, and all other indices are set to 0.