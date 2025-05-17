### Matrix times Matrix

multiply two matrices together (return -1 if shapes of matrix dont aline), i.e.
C=A⋅B

**Example:**

Input:
```
A = [[1,2],[2,4]], B = [[2,1],[3,4]]
```

Output:
```
[[ 8,  9],
 [16, 18]]
```

Reasoning:

1*2 + 2*3 = 8; 2*2 + 3*4 = 16; 1*1 + 2*4 = 9; 2*1 + 4*4 = 18 
Example 2: input: A = [[1,2], [2,4]], B = [[2,1], [3,4], [4,5]] output: -1 
reasoning: the length of the rows of A does not equal the column length of B