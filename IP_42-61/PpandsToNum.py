# Write a Python Pandas program to convert a Pandas series to Numpy array.


import numpy as np 
import pandas as pd

# l=[1,2,4,5,10,26,87]
# arr=np.array(l)
# print(arr)
df=pd.Series([10,20,30,40,50])
arr=np.array(df)
print(arr)