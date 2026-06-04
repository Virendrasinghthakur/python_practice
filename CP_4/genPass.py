# Write A Python Program to Generate a Strong Password, Length should be provided from user.

import  random
import string
length=int(input('enter the length of password:'))
strs=string.ascii_lowercase+ string.digits
password=''.join(random.choice(strs) for _ in range(length))

print(password)