# Write a Python Program to remove any specific element from array using OOP.

import numpy as np
class array:
    def rem(self,arr):
        for i in range(arr.size-1):
            if arr[i]==19:
                arr=np.delete(arr,i)
        return arr

arr=np.array([10,20,30,15,19,17,14])
a=array()
print(a.rem(arr))
print(arr)