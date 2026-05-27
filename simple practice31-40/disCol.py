# Write A Python Program To Get 5 Color name From The User In List, Display That List, Remove Last Color And Then Display All The Colors to User
 
# l=[i for i in input("enter your colors :").split()]
# print(l)

l=[input("enter your color:") for i in range(5)]
print(l)
l.pop()
print(f"list after removing lastelement is {l}")