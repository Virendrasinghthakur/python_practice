# Write A Python Program To Get 4 Number From User And Put In The Following Equation:
# d+a+2ab/d(4c+10)
a,b,c,d=map(int,input("Enter the value of a b c d:").split())
ex=d+a+2*a*b/d*(4*c+10)
print(f"Value after performing the expression d+a+2ab/d(4c+10) is {ex:.0f}")
