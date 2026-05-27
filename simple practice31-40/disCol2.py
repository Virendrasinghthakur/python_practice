# Write A Python Program To Get 5 Color name From The User In List, Display That List, Remove First Color And Then Display All The Colors to User


l=[input("enter your color:") for i in range(5)]
print(l)
l.remove(l[0])
print(f"list after removing lastelement is {l}")