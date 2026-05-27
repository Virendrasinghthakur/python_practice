# // Write A Python Program To Find Area Of Triangle And Then Get A Number From The User, Find Square Of That Number. Then Add With Area Of The Triangle. Total Result Display To User

b,h=map(int,input("enter the base and height of the triangle :").split())
area=1/2*b*h
n=int(input("enter the number to be added :"))
sqr=n*n
sum1=area+sqr
print(f"The area of the traingle with the base{b} and height {h} is {area} srq units.And srq of the given number is {sqr} adn by adding with area it becomes {sum1}")