# Write a Python program that matches a string that has an ‘m or M' followed by anything, ending in ‘0 or 1'.

import re
s="mjhbvdsfiyg8e7384&*%^$0"

if re.match(r'^[mM].*[01]$',s):
    print("match found")
else:
    print("NO match found")