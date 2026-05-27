
# password strength checker 
password=input("enter your password :")
size=len(password)
passw="None"
if size<6:
    passw="Weak"
elif 6<size and 10>size:
    passw="medium"
else:
    passw="strong"
print(f"your password is in {passw} category")
