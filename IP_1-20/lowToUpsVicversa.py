# Write a Python Program To Get a word from user. The word should contain lower and uppercase both. Then convert lower to upper and upper to lower.


word="heLlo"
new=""
for i in range(len(word)):
    if word[i].islower():
        new+=word[i].upper()
    else:
        new+=word[i].lower()

print(new)