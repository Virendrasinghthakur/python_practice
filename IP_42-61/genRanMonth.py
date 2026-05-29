# Write a Python Program to Generate a random month between start and end date.

import random
from datetime import datetime,timedelta

s_date=datetime(2023,1,1)
e_date=datetime(2023,12,31)

random_month=random.randint(s_date.month,e_date.month)
# print("random month :",random_month)
# print(random_month.strftime("%B"))
random_date=s_date+ timedelta(days=random.randint(0,(e_date-s_date).days))
print(random_date)
# random_date=random.randint(s_date.date-e_date.date).days
# print("random date",random_date)


