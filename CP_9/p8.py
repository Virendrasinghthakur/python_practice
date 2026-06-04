# Write a regular expression Program in Python to search following pattern inside a string: anythingNumber_Uppercase
import re

p="vee123_A"

if re.search(r".*\d_[A-Z]",p):
    print("valid")
else:
    print("invalid")
    