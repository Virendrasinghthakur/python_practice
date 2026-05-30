# Write a Python Program to display odd number from array using OOP.


import numpy as np


class dis_odd:
    def cal_size(self,arr):
        
        return [int(i) for i in arr if i%2!=0]
    
arr=np.array([10,20,30,50,33,51])

a=dis_odd()
print(a.cal_size(arr))