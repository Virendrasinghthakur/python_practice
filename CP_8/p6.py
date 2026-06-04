# Write a Python program which match a string that contains uppercase, numbers, and underscores. It should not Ignore white space.

import re
s="35466f dv_A"
if re.match(r"^(?=.*[A-Z])(?=.*[a-z])(?=.[0-9])\S+$",s):
    print("string is valid")
else:
    print("string is not valid")