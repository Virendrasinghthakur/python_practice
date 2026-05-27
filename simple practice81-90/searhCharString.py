# Write A Python Program To Search Any Character (or Set of Character) From a String.

s="abcdefghijklmnopqrstuvwxyz"

c="v"
for i in range(len(s)):
    if c==s[i]:
        print(i+1)