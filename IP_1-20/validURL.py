# Write A Python Program To Get A URL from user to check whether it is valid URL or not.

url=input("enter the url :")

first="https://"
last=".com"
uf=url[:8]
lf=url[-4:]

print(uf,lf)
if first==uf and last==lf :
    print("URL is valid ")
else:
    print("not valid ")