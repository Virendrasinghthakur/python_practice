# Write a Python Program to Reverse array element using OOP.

import numpy as np
class array:
    def rev(self,arr):
        return arr[::-1]
arr=np.array([10,20,30,15,19,17,14])
a=array()
print(a.rev(arr))
print(arr)