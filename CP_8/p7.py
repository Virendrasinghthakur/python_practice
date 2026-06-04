# Write a Python program where a string will END with a number.

import re 

s="casgdfbdf6"

if re.search(r"[0-9]$",s):
    print('number is present at last')
else:
    print("no number  at last")