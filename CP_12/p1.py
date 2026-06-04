# WWrite a Python Program to make dictionary to a text file

dic={"a":"hii","b":"hi how are you ","c":"fine or not not doing well"}

with open("sample.txt","w") as f:
    f.write(str(dic))