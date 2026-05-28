# Write a Python NumPy program to make an array of equal shape having same data type of a given array.


import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

new_arr = np.zeros(arr.shape, dtype=arr.dtype)

print("Original Array:")
print(arr)

print("New Array:")
print(new_arr)