# Write a Python Program to display element of list with their occurrence using another method.

l=[1,1,2,3,5,5,5,7,9,8,7,9,5]

dic={}

for el in l:
    if el in dic.keys():
        dic[el]+=1
    else:
        dic[el]=1

for k,v in dic.items():
    print(f"the element is {k} and its count is {v}")


# print(l.count(5))