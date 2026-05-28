# Write a Python program to get the total length of all values of a dictionary with string values.

dic={
    "1":"Amit",
    "2":"Sumit",
    "3":"Ajay"
}
total=0
for val in dic.values():
    total+=len(val)
    
print(total)