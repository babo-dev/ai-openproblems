### Implementing Basic Autograd Operations

Special thanks to Andrej Karpathy for making a video about this, if you haven't already check out 
his videos on YouTube https://youtu.be/VMj-3S1tku0?si=gjlnFP4o3JRN9dTg. Write a Python class similar to 
the provided 'Value' class that implements the basic autograd operations: addition, multiplication, 
and ReLU activation. The class should handle scalar values and should correctly compute gradients for 
these operations through automatic differentiation.

**Example:**

Input:
```python
a = Value(2)
b = Value(-3)
c = Value(10)
d = a + b * c
e = d.relu()
e.backward()
print(a, b, c, d, e)
```

Output:
```python
Value(data=2, grad=0) Value(data=-3, grad=0) Value(data=10, grad=0)
```

Reasoning:

The output reflects the forward computation and gradients after backpropagation. 
The ReLU on 'd' zeros out its output and gradient due to the negative data value.