# write a program to store user name ,address and contact in a dictionary and upadte the number by asking from user on run time

name=input("enter your name :")
address=input("enter your address:")
cont=int(input("enter your contact number:"))
info={"Name ":name,
      "Address":address,
      "Contact":cont}
print(f"your available data is :{info}")
ncont=int(input("Please enter your new number to update :"))
info["Contact"]=ncont
print(f"your available data is :{info}")
