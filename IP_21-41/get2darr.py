import numpy as np

n=3
l=[]
for i in range(n):
    el=list(map(int,input("enter the elemetns:").split()))
    l.append(el)

arr=np.array(l)
print(arr)


