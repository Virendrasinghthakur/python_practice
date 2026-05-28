# Write a Python Program to create a nested dictionary. And Also iterate nested dictionary items


dics={}

# n=int(input("enter how many values you wan to input:"))
n=3

for i in range(n):
    key1=input("enter the key for nes dic:")
    dics[key1]={}
    for j in range(3):
        key=input(f"enter key in {i}dic:")
        value=input(f"enter values {i} dic:")
        dics[key1][key]=value

# dics={'a': {'1': '10', '2': '20', '3': '30'}, 'b': {'1': '10', '2': '20', '3': '30'}, 'c': {'1': '10', '2': '20', '3': '30'}}

for dic in dics.items():
    print(dic)
