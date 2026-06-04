# Write a Python program to check whether password is strong or weak.
import re
passw="Veersingh2006" 

if re.match(r"(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])",passw):
    print("password is strong")
else:
    print("password is weak")