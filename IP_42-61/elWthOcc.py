# Write a Python Program to Display element of list with their occurrence

l=[1,1,2,3,5,5,5,7,9,8,7,9,5]

l.sort()
count=1
for i in range(len(l)-1):
    if l[i]==l[i+1]:
        count+=1
    else:
        print(f"element is {l[i]} and its count is : {count}")
        count=1

