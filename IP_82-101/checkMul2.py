# Write a Python Program to get a number from user to check whether it is multiple of 2 and 3 or not using Procedural programming.


def is_div(n):
    if not n%2 and not n%3:
        return True
    return False


n=int(input("enter the number:"))
ans=is_div(n)
if ans:
    print(f"{n} is a multiple of 2 and 3 ")
else:
    print(f"{n} is not a multiple of 2 and 3")
