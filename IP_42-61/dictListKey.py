# Write a Python Program Create dictionary from list that display its square as key.



dic={}
l=[5,8,3,7]

for el in l:
    dic[el*el]=el


print(dic)