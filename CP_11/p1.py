# Write a Python Program to extract the html from the page.


import requests

url="https://vegamovie.pe/"

response=requests.get(url)

html=response.text
print(html)