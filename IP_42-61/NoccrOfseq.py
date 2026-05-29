# Write a Python Numpy Program to Find the number of occurrences of a sequence in a array

import numpy as np 
import pandas as pd


arr1 = np.array([10, 10, 30, 40, 20, 30, 40])
# arr2 = np.array([10, 20, 30, 40])


# count=np.count_nonzero(arr1==10)
# print(count)

unique,counts=np.unique(arr1,return_counts=True)

for elemen,count in zip(unique,counts):
    print(elemen,count)

s=pd.Series(arr1)
print(s.value_counts())