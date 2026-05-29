# Write a Python program to get the size, permissions, owner, device of a specified path.


import os

path="student.csv"

info=os.stat(path)

print("size",info.st_size,"bytes")
print("owner id ",info.st_uid,"bytes")
print("device id",info.st_dev,"bytes")
print("permission",oct(info.st_mode),"bytes")
