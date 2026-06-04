# Write a Python program to get 3 color code and color name from user to store in a dictionary and convert it into Python Pandas Series.

import pandas as pd

dic={}
for i in range(3):
    color=input("enter color name:")
    code=input("enter color code:")
    dic[color]=code

s=pd.Series(dic)
print(s)
