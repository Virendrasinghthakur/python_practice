# Write a Python Program to find average of 5 number using OOP.
class avg:
    def cal_avg(self,l):
        return sum(el for el in l)

l=[15,16,25,98,74]
a=avg()

print(f"the average of el of {l} is {a.cal_avg(l)/5}")