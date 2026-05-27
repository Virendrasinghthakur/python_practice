
num=int(input('enter your numbers :'))
flag=True
for i in range(2,num):
    if num%i==0:
        print("Number is not prime number ")
        flag=False
        break
if flag==True:
    print("Number is Prime ")
