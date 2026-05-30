# Write a Python Program to create a list on run time, display list element, and also find max and min item from list of integers using OOP.
class listi:
    def __init__(self):
        self.create_list()
    def create_list(self):
        l=list(map(int,input("enter el :").split()))
        self.lt=l
    def find_minMax(self):
        return [max(self.lt),min(self.lt)]


l=listi()
print(l.find_minMax())