# Write a NumPy program to create one-dimensional array, getting number element from user using while loop.
import numpy as np 
l=[]
n=0
while(n<5):
    s=int(input("enter the element:"))
    l.append(s)
    n+=1

print(np.array(l))
