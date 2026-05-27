# Write A Python Program To Get A Angle From The User And Find Its Sin And Cos Value In Radian And Then Convert Their Result Into Degree Unit
import math
angle=int(input("enter the angle :"))
rad=math.radians(angle)
deg=math.degrees(rad)
print("sin",math.sin(rad))
print("cos",math.cos(rad))
deg=math.degrees(rad)

print("sin deg",math.sin(deg))
print("cos deg ",math.cos(deg))