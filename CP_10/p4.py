# Write A Python Program To Find Union , Intersection And Difference Of Two Set. Find Sum Of All Items Of Union, Intersection And Difference.


s1={10,20,30,56}
s2={10,20,65,48}

it=s1.intersection(s2)
u=s1.union(s2)
d=s1.difference(s2)
print(sum(it))
print(sum(u))
print(sum(d))