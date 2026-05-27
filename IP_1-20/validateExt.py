# Write A Python Program To Check Extension Of A File, If File Extension Is “.mp3” Then Display A Message. “This File Is Not Allowed”
import os

file_name="a1.mp3"
ext=os.path.splitext(file_name)[1]

print(ext)
if ext=="mp3":
    print("This file is not allowed")
else:
    print("This file is allowed")

