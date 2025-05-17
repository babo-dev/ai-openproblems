### Calculate Covariance Matrix

Write a Python function to calculate the covariance matrix for a given set of vectors. 
The function should take a list of lists, where each inner list represents a feature 
with its observations, and return a covariance matrix as a list of lists. Additionally, 
provide test cases to verify the correctness of your implementation.

**Example:**

Input:
```
[[1, 2, 3], [4, 5, 6]]
```

Output:
```
[[1.0, 1.0], [1.0, 1.0]]
```

Reasoning:

The covariance between the two features is calculated based on their deviations from the mean. 
For the given vectors, both covariances are 1.0, resulting in a symmetric covariance matrix.


### Use cases of Covariance Matrix

- **Data Analysis** 
   - Help identify which features are positively or negatively correlated, aiding in feature selection and dimensionality reduction.
- **Feature Selection**
    -  If two features have a high covariance, they may provide similar information, and one of them can be removed to simplify the model
- **Signal Processing**
  -  Removing noise from audio signals by analyzing covariance between frequency components.