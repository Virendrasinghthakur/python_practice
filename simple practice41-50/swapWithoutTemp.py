# Write A Python Program To Get 2 Number From The User Store In Variable, Interchange Their Value, Without Creating Temp Variable

a,b=map(int,input("enter the a and b to swap values :").split())
print(f"value of a is {a} and b is {b} before swap ")
a,b=b,a
print(f"value of a is {a} and b is {b} after swap ")