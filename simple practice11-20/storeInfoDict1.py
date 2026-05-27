# write a program to store user name ,address and contact in a dictionary and upadte the number by asking from user

name=input("enter your name :")
address=input("enter your address:")
cont=int(input("enter your contact number:"))
info={"Name ":name,
      "Address":address,
      "Contact":cont}
print(f"your available data is :{info}")
ncont=65468435
info["Contact"]=ncont
print(f"your available data is :{info}")
