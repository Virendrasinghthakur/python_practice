# Write a Pandas program to convert a Panda module Series to Python list.

import pandas as pd
s=pd.Series([10,20,30,40,50])

l=list(s)

print(l)