# Write A Python Program Sort Dictionary By Key

dic = {"c":30,"a":10,"b":20}

keys=list(dic.keys())

keys.sort()

new_dic={}

for k in keys:
    new_dic[k]=dic[k]

print(new_dic)
