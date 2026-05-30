# Write a Python Program to count any array element from existed array using OOP

import numpy as np


class arr_size:
    def cal_size(self,arr):
        return arr.size
    
arr=np.array([10,20,30,50])

a=arr_size()
print(a.cal_size(arr))