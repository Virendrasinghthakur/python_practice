# Write A Python Program To Get A Email From The User And Make Sure That It Is Email In Proper Format Having @ Symbol And .

email=input("enter the email address :")
atvalid=False
dotvalid=False
for c in email:
    if c=="@":
        atvalid=True
    elif c==".":
        dotvalid=True

if atvalid and dotvalid :
    print("email is valid ")
else:
    print("not valid ")