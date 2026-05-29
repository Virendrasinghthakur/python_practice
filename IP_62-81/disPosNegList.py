# Write a Python Program to Display positive and negative in a list. When there is Positive and Negative number. Using list comprehension.

l=[10,20,-1,-50,26,65,-99]

pos=[el for el in l if el<0]
neg=[el for el in l if el>0]
print(f"positive in the given list are:{pos} and the negative are:{neg}")