### Softmax Activation Function Implementation

Write a Python function that computes the softmax activation for a given list of scores. 
The function should return the softmax values as a list, each rounded to four decimal places.

Example:

Input:
```python
scores = [1, 2, 3]
```

Output:
```
[0.0900, 0.2447, 0.6652]
```

Reasoning:

The softmax function converts a list of values into a probability distribution. 
The probabilities are proportional to the exponential of each element divided by the 
sum of the exponential of all elements in the list.