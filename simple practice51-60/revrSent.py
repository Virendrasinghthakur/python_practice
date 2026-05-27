# Write A Python Program To Get A Sentence From The User, To Reverse That Sentence
s=input("enter the sentence:")
l=len(s)
for i in range(l-1,-1,-1):
    print(s[i],end="")
