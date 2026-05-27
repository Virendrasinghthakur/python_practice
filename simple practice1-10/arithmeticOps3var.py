#  write a program to perform all arithmetic operations 3 variable


a,b,c=map(int,input("enter the value of a and b :").split())

print(f"Addition of {a} and {b} is : {a+b+c} ")

print(f"Subtraction of {a},{b} and {c} is : {abs(a-b-c)} ")
print(f"Multiplication of {a},{b} and {c} is : {a*b*c} ")
print(f"Division of {a},{b} and {c} is : {(a//b//c)} ")
print(f"Modules of {a},{b} and {c} is : {(a%b)%c} ")
