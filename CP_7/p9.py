# Write a Python program to check a to z, A- Z, 0 to 9 and _ from a user entered string at starting position.

import re

s = input("Enter a string: ")

if re.match(r'^[a-zA-Z0-9_]', s):
    print("Valid starting character")
else:
    print("Invalid starting character")