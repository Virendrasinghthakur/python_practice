# WAP get name of week and show "holiday" if user input sunday or friday.
day=input("enter the name of the day :")

if day.lower() in ("sunday","friday"):
    print("Today is Holiday")
else:
    print("Not a Holiday")
