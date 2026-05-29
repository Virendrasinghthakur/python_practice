# Write a Python Program Create dictionary from existed dictionary which display length of words as value


dic1={
    1:"hello",
    2:"hii",
    3:"sameer",
    4:"kabeer"
}

dic2={

}
for k,v in dic1.items():
    dic2[k]=len(v)


print(dic2)