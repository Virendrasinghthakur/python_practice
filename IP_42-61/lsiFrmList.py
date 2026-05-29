# Write a Python Program to Create list from existed list that count number less than 20 greater than 5

l=[15,20,17,19,2,3,89,56,14]

l1=[el for el in l if el>5 and el<20]

print(l1)