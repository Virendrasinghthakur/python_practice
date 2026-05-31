# Write a Python Program To Find Roots Of Quadratic Equation
import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

d = b**2 - 4*a*c

x1 = (-b + math.sqrt(d)) / (2*a)
x2 = (-b - math.sqrt(d)) / (2*a)

print("Root 1 =", x1)
print("Root 2 =", x2)