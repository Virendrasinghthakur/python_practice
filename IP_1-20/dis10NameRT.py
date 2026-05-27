# Write A Python Program To Get 10 Name Of The Students And Display Them On The Screen And User Able To Update Any Student On Run Time


l=list(input("enter your names :") for i in range(10))

for i in range(10):
    print(f"{l[i]} index is  {i}")

id=int(input("enter the index to update:"))
val=input("enter the new value :")

l[id]=val
for i in range(10):
    print(f"updated list items are {l[i]}")