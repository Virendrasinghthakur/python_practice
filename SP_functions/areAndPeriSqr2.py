# Write A Python Program To Find Area And Perimeter Of A Square Using Function 
#        (A = L2, P = 4a), Find Square Root Of Its Area And Perimeter And Add Both Result. And Display Final Result To User
def area(a:int):
    return 4*a

def peri(a:int):
    return 2*a

def sqr(a):
    guess=a/2
    for i in range(10):
        guess=(guess+a/guess)/2
    
    return guess
a=5

area=area(a)
peri=peri(a)
sqra=sqr(area)
sqrp=sqr(peri)
print(f"area of sqr with side {a} is {area}")
print(f"perimeter of sqr with side {a} is {peri}")
print(f"the sqrroot of the area is {sqra} and for perimeter is {sqrp} and their sum is : {sqra+sqrp} ")