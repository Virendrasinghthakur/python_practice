# Write a Python Program To find array size in bytes using OOP.

import numpy as np
class size:
    def cal_size(self,arr):
        return arr.nbytes
    

arr=np.array([10,20,30])
s=size()
print(s.cal_size(arr))
