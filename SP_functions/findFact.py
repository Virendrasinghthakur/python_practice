# Write A Python Program To Get A Number From The User To Find Factorial Of That Number
n=int(input("enter the number for factorial :"))
fact=1
for i in range(1,n+1):
    fact*=i

print("the factorial is:",fact)