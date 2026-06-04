# Write a Python Program to get file creation and modification date or time

import os
from datetime import datetime

file="Z:\letstart\Python_practice\Complex_problems"

creation_time=os.path.getctime(file)
m_time=os.path.getmtime(file)

print("creation time :",datetime.fromtimestamp(creation_time))
print("modification time :",datetime.fromtimestamp(m_time))

      