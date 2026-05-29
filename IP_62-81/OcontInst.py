# Write a Python Program to count number of instances of a Python class.

class student :
    count=0
    def __init__(self,name):
        self.name=name
        student.count+=1
        



s1=student("arrav")
s2=student("arrav")
s=student("arrav")

print(student.count)