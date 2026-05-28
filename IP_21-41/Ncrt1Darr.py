# Write a NumPy program to create one-dimensional array, getting number element from user using for loop.
import numpy as np
n=4
arr=[]
for i in range(4):
    el=int(input("enter elment:"))
    arr.append(el)

arr=np.array(arr)
print(arr)