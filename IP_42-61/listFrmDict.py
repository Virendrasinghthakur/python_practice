# Write a Python Program to Create list from existed dictionary that count values less than 20 greater than 5

dic={5: 25, 8: 64, 3: 9, 7: 49}

l=[el for el in dic.values() if el>5 and el<20]

print(l)
