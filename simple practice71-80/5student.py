# Write A Python Program To Store 5 Student Name In A List And Check If The First Char Of First Student Name Is Equal To Last Student’s First Char
l=[input("enter the names :") for i in range(5)]

if l[0][0]==l[-1][0]:
    print("yes it is equal")
else:
    print("No it is not equal")