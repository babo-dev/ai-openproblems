### Leaky ReLU Activation Function

Write a Python function leaky_relu that implements the Leaky Rectified Linear Unit (Leaky ReLU) activation function. 
The function should take a float z as input and an optional float alpha, with a default value of 0.01, 
as the slope for negative inputs. The function should return the value after applying the Leaky ReLU function.

**Example:**

Input:
```python
print(leaky_relu(0)) 
print(leaky_relu(1))
print(leaky_relu(-1)) 
print(leaky_relu(-2, alpha=0.1))
```

Output:
```
0
1
-0.01
-0.2
```

Reasoning:

For z = 0, the output is 0.
For z = 1, the output is 1.
For z = -1, the output is -0.01 (0.01 * -1).
For z = -2 with alpha = 0.1, the output is -0.2 (0.1 * -2).