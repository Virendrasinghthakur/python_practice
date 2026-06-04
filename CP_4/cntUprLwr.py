# Create  a Python Program to Count total number of Uppercase and Lowercase in a string.
s=input("enter the string :")

l=0
u=0
for c in s:
    if c.islower():
        l+=1
    elif c==" ":
        continue
    else:
        u+=1

print(f"total uppercases are {u} adn lower are {l}")