# Write a Python program to find a maximum value in a dictionary (having value with number data type)


dic={
    "1":100,
    "2":105,
    "3":101
}


max=0
for val in dic.values():
    if max<val:
        max=val

print(max)

