# Write a Python Program to create a list on run time, display list element, and also find max and min item from list of integers using Procedural Programming.

def create_list():
    l=list(map(int,input("enter el :").split()))
    return l
def find_minMax(lt):
    return [max(lt),min(lt)]

l=create_list()
print(f"list created succefully {l} and its max and min elements are {find_minMax(l)}")
