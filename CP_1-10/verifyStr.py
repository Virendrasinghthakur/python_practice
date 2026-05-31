# Write A Python Program To Get String From User To Display Required Character That Present On Odd Index Number. Required Character Get From User
s = input("Enter a string: ")
index = int(input("Enter an odd index: "))

if index % 2 != 0 and index < len(s):
    print("Character =", s[index])
else:
    print("Invalid odd index")