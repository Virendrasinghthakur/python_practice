# Write a Python program that matches a word containing ‘m'.

a="vsebrjkn"

flag=False
for c in a:
    if c=='m':
        flag=True

if not flag:
    print("No it is not valid")
else:

    print("yes it is valid ")
        