# Write a Python program to match a number and _ at the ending of a string.


import re 

s="casgdfbdf3_"

if re.search(r"\d_$",s):
    print('number is present at last')
else:
    print("no number  at last")