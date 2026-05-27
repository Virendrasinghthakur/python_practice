# Write A Python Program To Store Students Records, User Will Be Able To Delete Any Student From A Record On Run Time

dic={}

n=int(input("enter how many entries you wants ot enter :"))

for i in range(n):
    name=input("enter student name :")
    roll=input("enter the student roll no:")
    mob=int(input("enter the mobile number of student:"))
    dic[roll]={"name":name,"Mobile":mob}

r=input("Enter the roll number of student you want to remove:")

dic.pop(r)
print(dic)