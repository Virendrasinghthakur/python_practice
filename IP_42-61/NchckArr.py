# Write a Python Numpy Program to Check whether a array contains a specified row.
import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

row1=np.array([4,5,6])

# for row in arr:
#     print(row==row1)

if np.any(np.all(arr==row1,axis=1)):
    print("yes")
else:
    print("NO")