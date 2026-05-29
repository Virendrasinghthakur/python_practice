# Write a Python program to convert JSON into Python object.

import json

json_data = '{"name": "Virendra", "age": 20, "city": "Jaipur"}'


py=json.loads(json_data)
py1=json_data
print(py)
print(type(py1))