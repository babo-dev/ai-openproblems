### Implementation of Log Softmax Function

In machine learning and statistics, the softmax function is a generalization of the logistic 
function that converts a vector of scores into probabilities. The log-softmax function is the 
logarithm of the softmax function, and it is often used for numerical stability when computing 
the softmax of large numbers.

Given a 1D numpy array of scores, implement a Python function to compute the log-softmax of the array.

**Example:**

Input:
```python
A = np.array([1, 2, 3])
print(log_softmax(A))
```

Output:
```python
array([-2.4076, -1.4076, -0.4076])
```
Reasoning:

The log-softmax function is applied to the input array [1, 2, 3]. The output array contains the 
log-softmax values for each element.