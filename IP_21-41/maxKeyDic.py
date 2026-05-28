# Write a Python Program to find a maximum key in a dictionary (having key with number data type)


dic={
    1:"Amit",
    2:"Sumit",
    3:"Ajay"
}


max=0
for key in dic.keys():
    if max<key:
        max=key

print(max,dic[max])