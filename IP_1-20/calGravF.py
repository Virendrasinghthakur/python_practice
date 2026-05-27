# Write A Python Program To Find Gravitational Force


m1=int(input("enter the value of m1:"))
m2=int(input("enter the value of m2:"))
g=6.67*10**-11
r=int(input("enter the radius:"))

F=g*m1*m2/r**2

print("the force applied will be ",F,"N")