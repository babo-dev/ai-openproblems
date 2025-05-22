### Divide Dataset Based on Feature Threshold

Write a Python function to divide a dataset based on whether the value of a specified 
feature is greater than or equal to a given threshold. The function should return
two subsets of the dataset: one with samples that meet the condition and another 
with samples that do not.

**Example:**

Input:
```python
X = np.array([[1, 2], 
              [3, 4], 
              [5, 6], 
              [7, 8], 
              [9, 10]])
feature_i = 0
threshold = 5
```
Output:
```python
[array([[ 5,  6],
        [ 7,  8],
        [ 9, 10]]), 
 array([[1, 2],
        [3, 4]])]
```
Reasoning:

The dataset X is divided based on whether the value in the 0th feature (first column)
is greater than or equal to 5. Samples with the first column value >= 5 are in the 
first subset, and the rest are in the second subset.