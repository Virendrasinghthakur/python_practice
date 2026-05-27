# Write A Python Program Sort Dictionary By values

dic = {"c":30,"a":10,"b":20}

values=list(dic.items())
# values.sort([1])
print(values)


for i in range(len(values)):
    for j in range(len(values)-1-i):
        if values[j][1]>values[j+1][1]:
            values[j],values[j+1]=values[j+1],values[j]


sorted_dic=dict(values)
print(sorted_dic)
# values.sort()

# new_dic={}

# for val in values:
#     new_dic[k]=dic[k]

# print(new_dic)
