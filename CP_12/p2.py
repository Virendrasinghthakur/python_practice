#Write a Python Program to make List of students to a text file

l=["aman","mohit","ajay","sumit"]

with open("sample.txt","w") as f:
    f.write(str(l))