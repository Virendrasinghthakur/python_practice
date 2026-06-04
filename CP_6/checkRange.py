# Write a Python Program to get a alpha character from user to check whether it is in given range or not: range(a to f)

ch = input("Enter an alphabet: ").lower()

if 'a' <= ch <= 'f':
    print("Character is in the range a to f")
else:
    print("Character is not in the range a to f")
