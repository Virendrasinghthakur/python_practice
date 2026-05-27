# Write A Python Program To Get A Number From The User To Find Factorial Of That Number. Using another method as I discussed
# n=int(input("enter the number for factorial :"))

def fact(n):
    if n==1 or n==0:
        return 1

    return n*fact(n-1)
ans=fact(5)
print("the factorial is:",ans)