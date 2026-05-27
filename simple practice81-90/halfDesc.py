# Write A Python Program To Get A Number From User, The System Should Auto Decrement To That Number. Half Of User Entered Number Should Be Decremented
num = int(input("Enter a number: "))

half = num / 2

half -= 1   # auto increment

print("Half of the number after increment is:", half)