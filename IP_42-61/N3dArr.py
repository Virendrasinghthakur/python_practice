# Write a NumPy program to create a three dimension array with shape (3,4,4) and set to a variable

import numpy as np

# dims=[3,4,4]
# l=[]
# for i in range(dims[0]):
#     l1=[]
#     for j in range(dims[1]):
#         l2=[]
#         for k in range(dims[2]):
#             el=int(input("entr element:"))
#             l2.append(el)

#         l1.append(l2)
#     l.append(l1)


# arr=np.array(l)

# print(arr)


arr=np.arange(48).reshape(3,4,4)
print(arr)