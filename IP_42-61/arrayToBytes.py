# Write a Python NumPy program to convert an array to bytes and load it as array.
import numpy as np

arr=np.array([10,20,101,256,24])

arr1=arr.astype(bytes)
print(arr1)