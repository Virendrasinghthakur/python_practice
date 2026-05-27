# Write A Python Program To get first and last name from the user and display full name. Make chaptalize both (First and last name)
first,last=input("enter the first and last :").split()
print(f"first name is {first} and last name is {last} and full name is {first.capitalize() +" "+ last.capitalize() }")
