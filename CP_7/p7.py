# Write a Python program that find a string which have ‘m' char then anything (optional) and end at ‘0'.

s="mjhbvdsfiyg8e7384&*%^$0"

if s[0]=='m' and s[-1]=="0":
    print("match found")
else:
    print("NO match found")