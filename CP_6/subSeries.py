# Write a Pandas program to create a subset of a given series.
 
import pandas as pd

s=pd.Series([10,20,15,65,47,15,24,32])
s1=s[2:6]
print(s1)