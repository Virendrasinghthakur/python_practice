# Write a Python Program to get column names from CSV. Using another method.


import csv

with open("student.csv", "r") as file:
    reader = csv.reader(file)

    columns = next(reader)  

print("Column Names:", columns)