# Write a Python Program to Create set that display only odd number



s={10,20,30,15,19,25,16,17,15}

print(s)
# print(type(s))

for i in s:
    if i%2!=0:
        print(i,end=",")