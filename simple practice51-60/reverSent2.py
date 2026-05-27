# Write A Python Program To Get A Sentence From The User, To Reverse That Sentence And Enclose In Double Quotations And Put A Full Stop At The End Of Sentence
s=input("enter the sentence:")
l=len(s)
print('"',end="")
for i in range(l-1,-1,-1):
    print(s[i],end="")
print('"',end="")
print(".")