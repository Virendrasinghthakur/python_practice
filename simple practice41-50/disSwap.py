# Write A Python Program To Get 2 Number From The User, Find Their Cube, And Add Both Result, Finally Result Display To User.
a,b=map(int,input("enter the a and b to swap values :").split())
print(f"value of a is {a} and b is {b} before swap ")
temp=a
a=b
b=temp
print(f"value of a is {a} and b is {b} after swap ")