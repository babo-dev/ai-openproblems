### Decision Tree Learning

Write a Python function that implements the decision tree learning algorithm for classification. 
The function should use recursive binary splitting based on entropy and information gain to build
a decision tree. It should take a list of examples (each example is a dict of attribute-value pairs) 
and a list of attribute names as input, and return a nested dictionary representing the decision tree.

**Example:**

Input:
```python
examples = [
                    {'Outlook': 'Sunny', 'Temperature': 'Hot', 'Humidity': 'High', 'Wind': 'Weak', 'PlayTennis': 'No'},
                    {'Outlook': 'Sunny', 'Temperature': 'Hot', 'Humidity': 'High', 'Wind': 'Strong', 'PlayTennis': 'No'},
                    {'Outlook': 'Overcast', 'Temperature': 'Hot', 'Humidity': 'High', 'Wind': 'Weak', 'PlayTennis': 'Yes'},
                    {'Outlook': 'Rain', 'Temperature': 'Mild', 'Humidity': 'High', 'Wind': 'Weak', 'PlayTennis': 'Yes'}
                ],
                attributes = ['Outlook', 'Temperature', 'Humidity', 'Wind']
```

Output:
```
{
            'Outlook': {
                'Sunny': {'Humidity': {'High': 'No', 'Normal': 'Yes'}},
                'Overcast': 'Yes',
                'Rain': {'Wind': {'Weak': 'Yes', 'Strong': 'No'}}
            }
        }
```

Reasoning:

Using the given examples, the decision tree algorithm determines that 'Outlook' is the best attribute 
to split the data initially. When 'Outlook' is 'Overcast', the outcome is always 'Yes', so it becomes 
a leaf node. In cases of 'Sunny' and 'Rain', it further splits based on 'Humidity' and 'Wind', respectively. 
The resulting tree structure is able to classify the training examples 
with the attributes 'Outlook', 'Temperature', 'Humidity', and 'Wind'.