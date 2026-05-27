# Write A Python Program To Generate A Strong Password, Password Length Should Be Decided By User.

import random
import string
len=int(input("enter the length of the password to be generated:"))

chars=string.ascii_letters +string.digits+ string.punctuation

password=""

for i in range(len):
    password+=random.choice(chars)

print("generated password is :",password)