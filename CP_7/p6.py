# Write a Python program to find the sequences of lowercase and UPPERCASE letters. Uppercase should be at end.

s="abcAABBC"

ups=""
low=""
for ch in s:
    if ch.isupper():
        ups+=ch
    elif ch.islower():
        low+=ch


if s==low+ups:
    print("string is valid")
else:
    print("string is  not valid")