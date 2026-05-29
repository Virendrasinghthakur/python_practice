# Write a Python Program Create dictionary which display length of words as key. It should display length of value.


dic1 = {
    1: "hello",
    2: "hii",
    3: "sameer",
    4: "kabeer"
}

dic2 = {}

for k, v in dic1.items():
    length = len(v)
    
    if length not in dic2:
        dic2[length] = []
    
    dic2[length].append(v)

print(dic2)