# Write a Python Program to Open the URL using other than urllib library

import requests

url = "https://www.python.org"

response = requests.get(url)

print(response.text)