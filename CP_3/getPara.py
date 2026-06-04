# Write A Python Program To Get A Paragraph From User, To Find(total Char, without space total char, Total Words And Spaces)


para=input("enter the para:")

ccount=0
cs=0
s=0
tw=0

for c in para:
    words=""
    if c!=" ":
        words+=c
        cs+=1
    else:
        s+=1
        tw+=1
        words=""

    ccount+=1

print(f"total char are {ccount},total chars without space are {cs}, total spaces are {s}, and total words are {tw }")

