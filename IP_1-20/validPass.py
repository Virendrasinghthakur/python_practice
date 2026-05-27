# Write A Python Program To Get Password From The User That Contain Alpha Numeric, Special Characters, And More Than 8 And Less Than 20 Characters And Restrict User If User Include Uppercase Letter And Space



passw=input("enter the password:")
digit=False
alpha=True
spec=False
for c in passw:
    if c.isdigit():
        digit=True
    elif c.isalpha():
        alpha=True
    elif c.isupper():
        print("uppercases are not allowed!")
        break
    else:
        spec=True

if digit and alpha and spec:

    print("your password is valid ")
else:
    print("invalid password")