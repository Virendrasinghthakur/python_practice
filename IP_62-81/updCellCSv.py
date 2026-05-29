# Write a Python Program to Update cell value of CSV.

import csv 

with open("student.csv","r") as file:
    data=list(csv.reader(file))

print(data)

data[2][1]="22"

print(data)

with open("student.csv", "w") as file:
    writer=csv.writer(file)
    writer.writerows(data)

print("updated successfully")
