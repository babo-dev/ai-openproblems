## Calculate Root Mean Square Error (RMSE)

**Task: Compute Root Mean Square Error (RMSE)**

In this task, you are required to implement a function rmse(y_true, y_pred) that calculates 
the Root Mean Square Error (RMSE) between the actual values and the predicted values. RMSE is a commonly used metric 
for evaluating the accuracy of regression models, providing insight into the standard deviation of residuals.

**Example:**

Input:
```python
y_true = np.array([3, -0.5, 2, 7])
y_pred = np.array([2.5, 0.0, 2, 8])
print(rmse(y_true, y_pred))
```

Output:
```
0.612
```

Reasoning:

The RMSE is calculated as sqrt((0.5^2 + 0.5^2 + 0^2 + 1^2) / 4) = 0.612