# Write a Python Program to display only those number that are divisible by 4 or 5 from list, using list comprehension.

l=[10,20,30,15,17,19,100,60]

print([el for el in l if el%4==0 or el%5==0])