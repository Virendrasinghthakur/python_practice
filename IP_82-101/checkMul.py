# Write a Python Program to get a number from user to check whether it is multiple of 5 or not using Procedural programming.


class mul:
    def is_div(self,n):
        if not n%5:
            return True
        return False
    

n=int(input("enter the number:"))
d=mul()
ans=d.is_div(n)
if ans:
    print(f"{n} is a multiple of 5")
else:
    print(f"{n} is not a multiple of 5")
