# Write a Python Program to Create a Dictionary to find addition of all the keys and Product of all the values from a dictionary.


dic={
    1:10,2:20,3:30
}


add=0
pro=1

for key,value in dic.items():
    add+=key
    pro*=value

print(add,pro)