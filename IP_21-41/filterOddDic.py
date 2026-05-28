# Write a Python program to filter odd numbers from a given dictionary keys. Display only those values which have odd keys.

dic={
    1:"Amit",
    2:"Sumit",
    3:"Ajay"
}
for key in dic.keys():
    if key%2!=0:
        print(key,dic[key])
    
    
