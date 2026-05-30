# Write a Python program to get a year from user to check it is leap year or not using OOP

class leap:
    def __init__(self,year):
        self.year=int(year)

    def isleap(self)->bool:

        if self.year%4==0 and self.year%400==0:
            return True
        return False
    

s=leap(2000)
print(s.isleap())