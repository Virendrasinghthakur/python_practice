# Write a Python program to access multiple elements from a tuple. Starting index and ending index provided by user.
tup=(10,20,'hello','nice','free',67,80)

st,lt=map(int,input("enter the starting and the ending index of the tuple:").split())

for i in range(st,lt+1):
    print(tup[i])