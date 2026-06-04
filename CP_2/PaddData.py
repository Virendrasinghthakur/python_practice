# Write a Pandas Program To Add Some Data To An Existing Series.
import pandas as pd

s=pd.Series([10,20,30,40])
s1=pd.Series([10,20,30])
s=pd.concat([s,s1],ignore_index=True)
print(s)