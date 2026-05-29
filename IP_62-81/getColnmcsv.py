# Write a Python Program to get column names from CSV.


import csv

with open("student.csv","r")as file:
    data=list(csv.reader(file))

print(data[0])