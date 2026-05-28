# Write a Python program to get 5 number from user to store in a list.  Add all that number to each other using list comprehension.

l=[(int(input("enter el:"))) for i in range(5)]

sl=[ el+2 for el in l]
print(sl)
total=sum([i for i in l])
print("Sum",total)

