# Write A Python Program To Find Maximum Number From A List Using Function 
def maxFromList(l):
    max=float('-inf')
    for c in l:
        if c>max:
            max=c
    return max

l={10,20,55,60,85}
print(f"Max element from the list {l} is {maxFromList(l)}")