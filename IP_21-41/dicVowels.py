# Write a Python Program to Create a dictionary which display those value which have vowel character.

dic = {
    1: "apple",
    2: "sky",
    3: "orange",
    4: "fly"
}

l={k:v for k,v in dic.items() if any(c in "aeiouAEIOU" for c in v)}
for k,v in dic.items():
    if v in "aeiou":
        print(k," ",v)

print(l)

