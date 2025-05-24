### Calculate Correlation Matrix

Write a Python function to calculate the correlation matrix for a given dataset. The function 
should take in a 2D numpy array X and an optional 2D numpy array Y. If Y is not provided, the 
function should calculate the correlation matrix of X with itself. It should return the correlation 
matrix as a 2D numpy array.

**Example:**

Input:
```python
X = np.array([[1, 2],
              [3, 4],
              [5, 6]])
output = calculate_correlation_matrix(X)
print(output)
```

Output:
```
[[1. 1.]
 [1. 1.]]
```
Reasoning:

The function calculates the correlation matrix for the dataset X. In this example, the correlation 
between the two features is 1, indicating a perfect linear relationship.