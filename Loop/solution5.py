# find the first non reapated character
s="hellowordhowareyou"
dic={}
for c in s:
    if c in dic:
        dic[c]+=1
    else:
        dic[c]=1

for key in dic:
    if dic[key]==1:
        print(key)
        break
print(dic)