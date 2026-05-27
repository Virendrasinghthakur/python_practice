# Write a Python program to create a destructor.
class student:
    def __init__(self):
        print("constructor is called ")

    def __del__(self):
        print("destructor is called ")

s=student()

del s