#Write a Python Program to extract the html from the page. Using other than our method.

import urllib.request
url=""

response=urllib.request.urlopen(url)
html=response.read().decode("utf-8")

print(html)