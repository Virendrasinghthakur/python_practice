# Write Python Program To Find Number Of Day Between Two Dates
n=10
binary=""
while n>0:
    rem=n%2
    binary=str(rem)+binary
    n=n//2
print(binary)