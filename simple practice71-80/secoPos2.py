# Write A Python Program To Find The Second Position Of A Student In A List. And Display Student Marks And Student Name

dic={
    "rohit":85,
    "mohit":78,
    "smay":77,
    "veer":88,
    "kartik":58
}

name=list(dic.keys())
print(f"the second student is {name[1]} and his marks are {dic[name[1]]}")