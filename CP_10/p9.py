# Write a Python Program to Open the url using urllib library

import urllib.request

url=""

response=urllib.request.urlopen(url)

data=response.read()
print(data.decode("utf-8"))
