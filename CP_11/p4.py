# Write a Python Program to display title of any web page using web scraping. With other method 

import requests
from bs4 import BeautifulSoup

url="https://vegamovie.pe/"

html=requests.get(url).text
soup=BeautifulSoup(html,'html.parser')

title=soup.find("title")

print(title.text)