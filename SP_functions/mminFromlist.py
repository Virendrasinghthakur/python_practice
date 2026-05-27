# Write A Python Program To Find Minimum Number From A List Using Function 
def minFromList(l):
    min=float('inf')
    for c in l:
        if c<min:
            min=c
    return min

l={10,20,55,60,85}
print(f"Min element from the list {l} is {minFromList(l)}")