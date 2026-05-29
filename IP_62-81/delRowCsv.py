# Write a Python Program to delete any row in a CSV file

import csv

with open("student.csv","r")as file:
    data=list(csv.reader(file))

print(data)
del data[1]
print(data)


with open("student.csv","w",newline="")as file:
    writer=csv.writer(file)
    writer.writerows(data)
    print("data saved succesfully")