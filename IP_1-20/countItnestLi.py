# Write a Python program to count any item from a nested list.
l = [
    [1, 2, 3],
    [4, 2, 6],
    [2, 8, 9]
]

item = int(input("Enter item to count: "))

count = 0

for row in l:

    for value in row:

        if value == item:

            count += 1

print("Total occurrence:", count)