# Write A Python Program To  Make a percentage calculator. 
l=list(map(int,input("enter your numbers :").split()))
print(f"Average of these numbers {l} is {sum(l)} {(sum(l)%len(l)*100)*100}")