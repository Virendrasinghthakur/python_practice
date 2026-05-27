# Write A Python Program To Find Coulomb Force between two charges.

q1=int(input("enter the value of q1:"))
q2=int(input("enter the value of q2:"))
f=9*10**9
r=int(input("enter the radius:"))

F=f*q1*q2/r**2

print("the force applied will be ",F,"N")