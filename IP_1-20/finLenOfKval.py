# Write a Python Program To Find Total Length Of Values And Keys In a Dictionary


dic={"1":"veer",
     "2":"ajay",
    "3":"sameer"
}

keyl=0
vl=0
for key,value in dic.items():
    keyl+=len(key)
    vl+=len(value)

print(keyl,vl)