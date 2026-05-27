# Write A Python Program To Get 3 Number From User And Put In The Following Equation:
	# a+b+ca/b(2a + 3b)

a,b,c=map(int,input("Enter the value of a b c :").split())
ex=a+b+c*a/b*(2*a+3*b)
print(f"Value after performing the expression a+b+ca/b(2a+3b) is {ex:.0f}")
