# Write a Python program to read a CSV file as a list using another method.

import csv

with open("student.csv", "r") as file:
    reader = csv.reader(file)
    data = [row for row in reader]

print(data)