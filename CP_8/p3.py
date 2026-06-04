# Write a Python program that matches a word containing ‘6‘ digit.

import re
s="hjabkf635"

if re.search(r"6",s):
    print("6 is present")

else:
    print("not in string")