# Write a Python program to multiply with every number with user entered number in a list.  When Number is Even

l=[10,20,7,9]

l1=[l[i]*2 for i in range(len(l)) if l[i]%2==0]

print(l1)