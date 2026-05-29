# Write a Python Program to Create a dictionary from list that display its square as value.
# dic1 = {
#     1: 5,
#     2: 8,
#     3: 3,
#     4: 7
# }

dic={}
l=[5,8,3,7]

for el in l:
    dic[el]=el*el


print(dic)