# Write a Numpy Program To Create a Two-dimensional Array & Multiply with any number to that array elements. That number take from user.

import numpy as np
# arr=np.array([1,8,6,9,12,3])

l=[]

for i in range(3):
    el=[int(input(i)) for i in range(3)]

    l.append(el)

arr=np.array(l)
n=int(input("entr the number to be multiplies:"))
print(arr*n)