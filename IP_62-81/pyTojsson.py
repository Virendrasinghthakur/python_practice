# Write a Python program to take Python data from user to convert into JSON Data.


import json

json_data = {"name": "Virendra", "age": 20, "city": "Jaipur"}


py=json.dumps(json_data)
py1=json_data
print(py)
print(type(py))