# Write A Python Program To Create A List To Pass To Function As Parameter To Display Its Element In Reverse Order.
l=[input("enter el:") for i in range(5)]

for i in range(len(l),-1,-1):
    print(l[i])