# Write a Python Pandas program to compare two Numpy array.

import pandas as pd
import numpy as np

arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([10, 20, 35, 40])

s1 = pd.Series(arr1)
s2 = pd.Series(arr2)
print(s1==s2)
print(s1.equals(s2))