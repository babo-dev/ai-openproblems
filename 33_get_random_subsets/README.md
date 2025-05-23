Generate Random Subsets of a Dataset

Write a Python function to generate random subsets of a given dataset. The function 
should take in a 2D numpy array X, a 1D numpy array y, an integer n_subsets, 
and a boolean replacements. It should return a list of n_subsets random subsets of 
the dataset, where each subset is a tuple of (X_subset, y_subset). If replacements is True, 
the subsets should be created with replacements; otherwise, without replacements.

**Example:**

Input:
```python
X = np.array([[1, 2],
              [3, 4],
              [5, 6],
              [7, 8],
              [9, 10]])
y = np.array([1, 2, 3, 4, 5])
n_subsets = 3
replacements = False
get_random_subsets(X, y, n_subsets, replacements)
```
Output:
```python
[array([[7, 8],
        [1, 2]]), 
 array([4, 1])]
 
[array([[9, 10],
        [5, 6]]), 
 array([5, 3])]
 
[array([[3, 4],
        [5, 6]]), 
 array([2, 3])]
```
Reasoning:
The function generates three random subsets of the dataset without replacements. Each subset includes 
50% of the samples (since replacements=False). The samples are randomly selected without duplication.