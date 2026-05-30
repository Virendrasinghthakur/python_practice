# Write a Python Program to find minimum number from array.


import numpy as np
arr=np.array([10,20,30,15,19,17,14])
max1=float('inf')

for el in arr:
    max1=min(el,max1)
print(max1)