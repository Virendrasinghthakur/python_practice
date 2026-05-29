# Write a Python program to insert an element after each element of a list.


l=[10,20,30,40]

el=5

rs=[]

for elm in l:
    rs.append(elm)
    rs.append(el)

print(rs)