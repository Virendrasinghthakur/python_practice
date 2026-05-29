# Write a Python Numpy program to create a array, store in a text file and display the result.


import numpy as np

arr=np.array([0,1,0,1,1])

if np.savetxt("arr.txt",arr):
    print("saved succefully")