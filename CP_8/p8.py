# Write a Python program to match a number 0 to 5 at the ending of a string.


import re 

s="casgdfbdf3"

if re.search(r"[0-5]$",s):
    print('number is present at last')
else:
    print("no number  at last")