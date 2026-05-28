# Write a Python program to convert dictionary’s keys and values into two tuple. One tuple should store keys and other tuple should store values.

dic={
    "1":"Amit",
    "2":"Sumit",
    "3":"Ajay"
}

# key=[i for i in dic.keys()]
# values=[i for i in dic.values()]

# key=tuple(dic.keys())
# values=tuple(dic.values())


key=tuple(i for i in dic.keys())
values=tuple(i for i in dic.values())

print(key)
print(values)
