# Write a Python program to get the total length of all keys of a dictionary with string keys.

dic={
    "1":"Amit",
    "2":"Sumit",
    "3":"Ajay"
}
total=0
for key in dic.keys():
    total+=len(key)
    
print(total)