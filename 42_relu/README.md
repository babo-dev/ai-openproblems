### Implement ReLU Activation Function

Write a Python function relu that implements the Rectified Linear Unit (ReLU) activation function. The function should 
take a single float as input and return the value after applying the ReLU function. The ReLU function returns
the input if it's greater than 0, otherwise, it returns 0.

**Example:**

Input:
```python
print(relu(0)) 
print(relu(1)) 
print(relu(-1))
```

Output:
```
0
1
0
```

Reasoning:

The ReLU function is applied to the input values 0, 1, and -1. The output is 0 for negative values 
and the input value for non-negative values.