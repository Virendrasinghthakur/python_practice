# Write A Python Program To Get 10 Number From The User, Store Into List, Find Their Products And Sum. Then Add Both Result To Display To User

l=[int(input("enter the numbers"))  for i in range(10)]

sum1=sum(l)
prod=1
for el in l:
    prod*=el
print(f"The sum of all the elements of the list is {sum1} and the product for the same is {prod}")