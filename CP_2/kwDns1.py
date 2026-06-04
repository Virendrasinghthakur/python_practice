# Write A Python Program To Find Keyword Density In A Article. And Display A Message If Density Increase Up To 3%


s=input("enter the string:")
kw=input("enter the keyword:")

words=s.lower().split()
kwc=words.count(kw.lower())
density=((kwc/len(words))*100)
print(f"the density of keyword {kw} is {density:.1f}")

if density>3:
    print("Density is higher")
