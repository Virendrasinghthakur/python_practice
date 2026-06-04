# Write a Python Program to create an class with data members.

class Student:
    def __init__(self, name, age):
        self.name = name    
        self.age = age    

s1 = Student("Virendra", 22)

print(s1.name)
print(s1.age)