# Write a Python program to find the sequences of UPPERCASE and lowercase letters. Lowercase should be at end.
s="AABBCabc"

ups=""
low=""
for ch in s:
    if ch.isupper():
        ups+=ch
    elif ch.islower():
        low+=ch


if s==ups+low:
    print("string is valid")
else:
    print("string is  not valid")
        
