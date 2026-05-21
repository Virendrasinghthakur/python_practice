spe=input("""select pet species
          1.Dog
          2.Cat
          """)
age=int(input("enter the age of the pet :"))
if spe=="2":
    if age<5:
        print("Baby cat food is suggested")
    else:
        print("senior cat food is suggested")
elif spe=="1":
    if age<5:
        print("Puppy food is suggested")
    else:
        print("senior dog food is suggested")
else:
    print("Please select a valid species ")