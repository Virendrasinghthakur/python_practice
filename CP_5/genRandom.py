# Write A Python Program To Generate Random Number , And Display Message If Required Number Matched. Required Number Will Be Taken From User

import random
num=int(input("enter a nmber from 1 to 10:"))

num1=random.randint(1,10)

if num==num1:
    print("your guess was right")
else:
    print('sorry you are wrong')