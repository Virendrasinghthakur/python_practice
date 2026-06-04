# Write a Python Program to check file size. Display message if file size between 3 to 5 Mb.
 
import os 

f="sample.txt"

s=os.path.getsize(f)

if s//1024>3 and s//1024<5:
    print("file size is valid")
else:
    print("not a valid size")