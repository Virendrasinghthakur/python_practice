# Write a Python Numpy Program to create a one dimensional array element. Then convert to list and then to tuple.
import numpy as np
arr = np.array([1, 2, 3, 4])

l=arr.tolist()
print(l)
l1=tuple(arr)
print(l1)
