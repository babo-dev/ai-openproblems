### Matrix-Vector Dot Product

Write a Python function that computes the dot product of a matrix and a vector. 
The function should return a list representing the resulting vector if the operation is valid, 
or -1 if the matrix and vector dimensions are incompatible. A matrix (a list of lists) can be dotted 
with a vector (a list) only if the number of columns in the matrix equals the length of the vector. 
For example, an n x m matrix requires a vector of length m.

**Example**:

Input:
```
a = [[1, 2], [2, 4]], b = [1, 2]
```

Output:
```
[5, 10]
```

Reasoning:

`Row 1: (1 * 1) + (2 * 2) = 1 + 4 = 5; Row 2: (1 * 2) + (2 * 4) = 2 + 8 = 10`
