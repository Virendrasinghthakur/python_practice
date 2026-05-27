# Write A Python Program To Get a Angle From The User And Find Its Sin And Cos Value In Radian
import math
angle=int(input("enter the angle :"))
rad=math.radians(angle)
print("sin",math.sin(rad))
print("cos",math.cos(rad))