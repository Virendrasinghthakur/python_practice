# Write a Python program where a string will start with a specific number.
import re

s="978csfdb"
if re.match(r"^5",s):
    print("string is valid ")
else:
    print("string is not valid")