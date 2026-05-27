# Write a Python program to print a list from a nested list which have lowest number.

l = [
    [1, 2, 3],
    [4, 2, 6,17],
    [2, 8, 9,18]
]

mini=float('inf')
min=float('inf')
for el in l:
    if len(el)<mini:
        mini=len(el)
        min=el
print(min)