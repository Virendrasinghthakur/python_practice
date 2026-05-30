# Write a Python Program to remove any specific element from array.

import numpy as np

arr=np.array([10,20,30,15,19,17,14])

print(arr.size)
for i in range(arr.size-1):
    if arr[i]==19:
        arr=np.delete(arr,i)

print(arr)