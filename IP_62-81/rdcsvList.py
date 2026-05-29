# Write a Python program to read a CSV file as a list

import csv 

# data = [
#     ["Name", "Age", "City"],
#     ["Virendra", 20, "Jaipur"],
#     ["Rahul", 21, "Delhi"],
#     ["Amit", 22, "Mumbai"]
# ]

# with open("student.csv","w",newline="") as file:
#     writer=csv.writer(file)
#     writer.writerows(data)

# print("CSV file created ")

with open("student.csv","r") as file:
    s=csv.reader(file)
    data=list(s)
    

for row in data:
    print(row)