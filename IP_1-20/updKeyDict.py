# Write a Python Program To Update Specific Key In A Dictionary.
dic={"1":"veer",
     "2":"ajay",
    "3":"sameer"
}

print(dic)

n=input("enter the key you want to update :")
v=input("enter the updated value:")

dic[v]=dic[n]

del dic[n]

print(dic)