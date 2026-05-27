
# Transport mode selection
d=int(input("enter the distance :"))
if d<3:
    print("You can walk for that much")
elif 3<d and d<15:
    print("you can go with Bike")
elif d>15:
    print(" for such distance car is good option")
else:
    print("please enter a valid distance")