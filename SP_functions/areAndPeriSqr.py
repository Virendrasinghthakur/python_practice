# Write A Python Program To Find Area And Perimeter Of A Square Using Function 
#        (A = L2, P = 4a)
def area(a:int):
    return 4*a

def peri(a:int):
    return 2*a


a=5
print(f"area of sqr with side {a} is {area(a)}")
print(f"perimeter of sqr with side {a} is {peri(a)}")