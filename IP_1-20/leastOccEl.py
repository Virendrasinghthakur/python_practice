# Write a Python program to find less occurring element in a given list of numbers.

l=[12,15,15,18,18,12,20,32,32,12]
dic={}
for el in l:
    if el in dic:
        dic[el]+=1
    else:
        dic[el]=1
least=float('inf')
leastv=float('inf')
for key,value in dic.items():
    if leastv>value:
        least=key
        leastv=value


print(leastv,least)