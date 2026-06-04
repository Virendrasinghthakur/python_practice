# Write a Python Program for Binary Search
l = [1, 3, 4, 5, 25, 26, 64, 89]

def binary_search(l, a, s, e):
    if s > e:
        return -1

    mid = (s + e) // 2

    if l[mid] == a:
        return mid
    elif a < l[mid]:
        return binary_search(l, a, s, mid - 1)
    else:
        return binary_search(l, a, mid + 1, e)

a = 3

print(binary_search(l, a, 0, len(l) - 1))

