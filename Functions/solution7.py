
# write a function that takes variable number of arguments and return their sum
def sum(*args):
    s=0
    for i in args:
        s+=i
    return s
print(sum(10,20,15))