# Write a Python program to get 5 number from user to store in a list. Display all the numbers with power of 3 using list comprehension.

# l=list(map(int,input("enter the 5 number :").split()))
# s=[]
# for el in l:
#     sl=el**3
#     s.append(sl)
# print(s)

l=[(int(input("enter el")))**3 for i in range(5)]
print(l)