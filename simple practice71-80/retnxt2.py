# Write A Python Program To Get A Number From User To Return Its Next Number With Addition Of User Entered Number And Previous Number With Addition Of User Entered Number
n=int(input("enter a number:"))
next=n+1+n
prev=n-1+n
print(f"Prev number is {prev} and the next number is {next}")