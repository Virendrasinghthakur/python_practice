# Write a Numpy Program To Create a one dimensional array. Display only even number from array.
import numpy as np
arr=np.array([1,8,6,9,12,3])

for el in arr:
    if el%2==0:
        print(el)