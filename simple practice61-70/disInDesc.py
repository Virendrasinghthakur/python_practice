# Write A Python Program That Accepts Six Identity Numbers Of Students As Input And Display In Descending Order. 

l=list(map(int,input("enter six identity numbers:").split()))

l.sort(reverse=True)

print(l)