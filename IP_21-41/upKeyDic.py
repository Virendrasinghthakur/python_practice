# Write a Python Program to update any key in a dictionary on user request.

dic={
    "1":"Amit",
    "2":"Sumit",
    "3":"Ajay"
}

old,new=input("enter the old key and new key:").split()
dic[new]=dic[old]

print(dic)
dic.pop(old)
print(dic)

