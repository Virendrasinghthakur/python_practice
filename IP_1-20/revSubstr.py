# Write a Python Program to reverse a sub string from a string.

s="hello how are you "
st="how are you"

if st in s:
    rev=st[::-1]

    result=s.replace(st,rev)
    print("updated string :",result)

else:
    print("string not found :")

