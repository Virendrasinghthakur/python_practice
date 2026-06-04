# Write a Python program which match a string that contains uppercase,  lowercase char, numbers, and underscores. It Ignore white space, punctuation etc

# s="Veersingh16400" 

# up=False
# lc=False
# num=False
# ud=False


# for c in s:
#     if c.isupper():
#         up=True
#     elif c.islower():
#         lc=True
#     elif c.isnumeric():
#         num= True
#     elif c=="_":
#         ud=True

# if up and lc and num and ud :
#     print("string is completely valid ")
# else:
#     print(f"string is not fully valid ")


import re

s = "Veersingh_16400"

pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*_)[A-Za-z0-9_]+$'

if re.match(pattern, s):
    print("String is completely valid")
else:
    print("String is not fully valid")