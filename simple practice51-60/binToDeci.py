# Write A Python Program To make binary to decimal conversion calculator 

binary="1010"

decimal=0
power=0

for digit in reversed(binary):
    decimal+=int(digit)*(2**power)
    power+=1

print("decimal ",decimal)