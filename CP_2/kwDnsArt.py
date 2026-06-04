# Write a Python Program To Find Keyword Density In a Article

s=input("enter the string:")
kw=input("enter the keyword:")

words=s.lower().split()
kwc=words.count(kw.lower())
density=(kwc/len(words))*100
print(f"the density of keyword {kw} is {density:.1f}")


