# Write A Python Program To Get A Sentence From A User, User Should Able To Remove Any Character From A String

s = input("Enter your sentence: ")

c = "a"
new_str = ""

for ch in s:
    if ch != c:
        new_str += ch

print(new_str)