# Write a Python program to create a nested list and access nested list item.



n=int(input("enter the number of sublist:"))
lt=[]
for i in range(n):
    l=list(map(int,input("enter the element:").split()))
    lt.append(l)

# l = [
#     [1, 2, 3],
#     [4, 2, 6, 17],
#     [2, 8, 9, 18]
# ]

for i in range(len(lt)):
    for j in range(len(lt[i])):
        print(lt[i][j])