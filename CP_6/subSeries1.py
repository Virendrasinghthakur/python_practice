# Write a Pandas program to create a subset of a given series. Add some modification.


import pandas as pd

s=pd.Series([10,20,15,65,47,15,24,32])
s1=s[s>30]
s2=s1+10
print(s2)