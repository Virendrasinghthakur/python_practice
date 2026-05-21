# classify a person age group

age=int(input("enter your age :"))
if age<13 :
    print("user is a child ")
elif age>13 and age<=19:
    print("user is a Teenager")
elif age>20 and age<=59:
    print("user is an adult")
else:
    print("user is a senior citizen")