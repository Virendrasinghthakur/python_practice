# Write a Python Program to display positive, negative and Zero in a list. When there is positive, negative or Zero number. Using list comprehension.


l=[10,20,-1,-50,0,26,65,-99,0]

pos=[el for el in l if el<0]
neg=[el for el in l if el>0]
zero=[el for el in l if el==0]
print(f"positive in the given list are:{pos}, zeroees are {zero} and the negative are:{neg}")