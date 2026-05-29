# Write a Python Pandas program to find transpose of array

import pandas as pd
import numpy as np

arr=np.array([[10,20,30],[1,2,3],[100,200,300]])
# print(arr)
# print(arr.transpose())

df=pd.DataFrame(arr)
print(df)
print(df.T)
