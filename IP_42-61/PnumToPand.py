# Write a Python Pandas program to convert a Numpy array to a Pandas series.

import numpy as np 
import pandas as pd

l=[1,2,4,5,10,26,87]
arr=np.array(l)
print(arr)
df=pd.Series(arr)
print(df)