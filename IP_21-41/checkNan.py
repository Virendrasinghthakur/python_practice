# Write a Python Numpy program to check element whether it is NaN or not.

import numpy as np

# arr = np.array([1, 2, "nan", 4])

# for i in range(len(arr)):
#     if arr[i]=="nan":
#         print("value is nan at index",i)



arr = np.array([10, 20, np.nan, 40])

for i in arr:

    if np.isnan(i):
        print(i, "is NaN")

    else:
        print(i, "is not NaN")