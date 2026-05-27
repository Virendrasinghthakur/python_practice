# Write a Python program to access element from a nested list.

l = [
    [1, 2, 3],
    [4, 2, 6, 17],
    [2, 8, 9, 18]
]

for i in range(len(l)):
    for j in range(len(l[i])):
        print(l[i][j])