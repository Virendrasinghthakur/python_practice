# Write a Python Program to get 10 number from user to print minimum, maximum and starting, ending number to user.
l=[10,20,45,8,25,0,26,27,30]

min=float('inf')
max=float('-inf')
first=l[0]
end=l[-1]

for el in l:
    if min>el :
        min=el
    if max<el:
        max=el
    

print(min,max,first,end)
    