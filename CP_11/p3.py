# Write a Python Program to display title of any web page using web scraping.
 
import requests
from bs4 import BeautifulSoup

url="https://vegamovie.pe/"
response=requests.get(url)
soup=BeautifulSoup(response.text,"html.parser")
print("Title:",soup.title.text)