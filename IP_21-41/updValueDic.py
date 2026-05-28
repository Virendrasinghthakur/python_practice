# Write a Python Program to update any value in a dictionary on user request.

dic={
    "1":"Amit",
    "2":"Sumit",
    "3":"Ajay"
}


key,value=(input("enter the key for which you want to update and also enter the value:").split())
dic[key]=value

print(dic)