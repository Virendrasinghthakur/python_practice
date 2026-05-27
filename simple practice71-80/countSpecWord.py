# Write A Python Program To Get A Sentence From User, To Count Specific Word In A Sentence

s=input("enter your sentence :")

count=0
word=""
check="hii"
for c in s:
    if c==" ": 
        if word==check:
            count+=1
        word=""
    else:
        word+=c

if check==word:
    count+=1

print(count)