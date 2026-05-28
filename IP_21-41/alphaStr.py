# Write a Python program to create a alpha string based dictionary to print dictionary items in uppercase.

d = {}

n = int(input("Enter number of items: "))

for i in range(n):

    key = input("Enter key: ")
    value = input("Enter value: ")

    if key.isalpha() and value.isalpha():

        d[key.upper()] = value.upper()

print(d)