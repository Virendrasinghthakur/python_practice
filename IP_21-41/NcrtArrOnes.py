# Write a NumPy program to create a new array of given shape (4,3) and type, filled with ones. And make in such way, user give shape value on run time.

import numpy as np
n,m=map(int,input("enter the shape of matrix").split())
arr=np.zeros((n,m),dtype=int)
print(arr)