
items = ["apple", "banana", "orange", "apple", "mango"]
unique=set()
for item in items:
    if item in unique:
        print("duplicate :",item)
    else:
        unique.add(item)
