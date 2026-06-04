# Write a Python Program to Read content from one file and write it into another file.
path="Z:\letstart\Python_practice\CP_11\Questions_11.txt"
with open(path,"r") as f:
    data=f.read()

path1="sample.txt"
with open(path1,"w") as f:
    f.write(data)
