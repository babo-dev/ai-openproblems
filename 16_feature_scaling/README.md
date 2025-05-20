### Feature Scaling Implementation

Write a Python function that performs feature scaling on a dataset using both standardization and 
min-max normalization. The function should take a 2D NumPy array as input, where each row represents 
a data sample and each column represents a feature. It should return two 2D NumPy arrays: 
one scaled by standardization and one by min-max normalization. Make sure all results are rounded 
to the nearest 4th decimal.

**Example:**

Input:
```python
data = np.array([[1, 2], [3, 4], [5, 6]])
```

Output:
```
([[-1.2247, -1.2247], [0.0, 0.0], [1.2247, 1.2247]], [[0.0, 0.0], [0.5, 0.5], [1.0, 1.0]])
```

Reasoning:

Standardization rescales the feature to have a mean of 0 and a standard deviation of 1. 
Min-max normalization rescales the feature to a range of [0, 1], where the minimum feature 
value maps to 0 and the maximum to 1.