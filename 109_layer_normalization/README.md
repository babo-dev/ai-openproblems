## Implement Layer Normalization for Sequence Data

Implement a function to perform Layer Normalization on an input tensor. Given a 3D array representing batch_size, 
sequence length, and feature dimensions, normalize the data across the feature dimension for each sequence, 
then apply scaling and shifting parameters.

**Example:**

Input:
```python
np.random.seed(42)
X = np.random.randn(2, 2, 3)
gamma = np.ones(3).reshape(1, 1, -1)
beta = np.zeros(3).reshape(1, 1, -1)
layer_normalization(X, gamma, beta)
```

Output:
```
[[[ 0.47373971 -1.39079736  0.91705765]
  [ 1.41420326 -0.70711154 -0.70709172]]
 [[ 1.13192477  0.16823009 -1.30015486]
  [ 1.4141794  -0.70465482 -0.70952458]]]
 ```

Reasoning:

The function computes the mean and variance across the feature dimension (d_model=3) for each sequence, 
normalizes the input, then applies gamma=1 and beta=0, resulting in a normalized output with zero mean 
and unit variance scaled as is.