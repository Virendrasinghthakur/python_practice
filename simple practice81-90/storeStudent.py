# Write A Python Program To Get Name Of Different Students From User And Store In A List. Condition Is That, System Should Stored The Name Of Student That Start From Char ‘a’ And End At ‘a’ Char 


l=["abhay","amit","farhan","afiza"]
s=[]
for item in l:
    if item[0]=='a' and item[-1]=='a':
        s.append(item)

print(s)