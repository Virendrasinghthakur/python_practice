
#  Movie ticket price
age=int(input("enter your age :"))
day=input("""enter the number of day 
              1.Sunday
              2.Monday
              3.Tuesday
              4.Wednesday
              5.Thursday
              6.Friday
              7.Saturday""")
if age<18:
    price=8
else:
    price=12
if day=="4":
    price-=2
    print("you got a discount and the final price is :",price)
else:
    print("Sorry you don't get any discount and the final price is :",price)
