# Write a Python Program to get 5 number from user, store in a list, convert to pandas series to change their default index numbers to alpha.


import pandas as pd

l=[10,20,30,40,50]
s=pd.Series(l,index=['a','b','c','d','e'])
print(s)
