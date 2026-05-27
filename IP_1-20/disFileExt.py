# Write A Python Program To Get Any File With Extension, To Display Only That File Extension.

# import os 
# file_name="IP_1-20.txt"

# ext=os.path.splitext(file_name)[1]

# print(ext)

file_name="IP_1-20.txt"
ext=""
found_dot=False
for c in file_name:
    if c==".":
        found_dot=True
    if found_dot :
        ext+=c

print(f"the extension of the file is {ext}")