# Write a Python Program to get file creation date or time

import os
import time 
file="Z:\letstart\Python_practice\Complex_problems"

creation_time=os.path.getctime(file)
print("Creation time:",time.ctime(creation_time))