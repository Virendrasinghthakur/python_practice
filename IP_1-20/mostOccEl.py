# Write a Python program to find most occurring element in a given list of numbers.

l=[12,15,18,12,20,32,12]
dic={}
for el in l:
    if el in dic:
        dic[el]+=1
    else:
        dic[el]=1
max=0
maxv=0
for key,value in dic.items():
    if max<value:
        max=key
        maxv=value


print(maxv,max)