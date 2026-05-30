# Write a Python Program to find addition of list element to create a new list. Add element of list as 1st and 2nd….  Using OOP.


class lst:
    def new_list(self,l,l1):
        for i in range(len(l)-1):
            a=l[i]+l[i+1]
            l1.append(a)
        return l1

l1=[]
l=[0, 25, 36, 48, 7895, 5246]
lt=lst()
print(lt.new_list(l,l1))