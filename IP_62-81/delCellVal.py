# Write a Python Program to Delete cell value of CSV.


import csv 

with open("student.csv","r") as file:
    data=list(csv.reader(file))


data[2][1]=""

print(data[2][1])
# with open("student.csv","w") as file:
#     writer=csv.writer(file)

#     writer.writerows(data)

#     print(data)

