# Write a Python Program to find addition of list element to create a new list. Add element of list as 1st and 2nd, 2nd and 3rd, 3rd and 4th …

l=[0, 25, 36, 48, 7895, 5246]
l1=[]

for i in range(len(l)-1):
    a=l[i]+l[i+1]
    l1.append(a)

print(l1)