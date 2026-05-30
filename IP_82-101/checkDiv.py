# Write a Python Program to get a number from user to check whether it is divisible by 5 or not using OOP.

class div:
    def is_div(self,n):
        if not n%5:
            return True
        return False
    
d=div()
print(d.is_div(15))