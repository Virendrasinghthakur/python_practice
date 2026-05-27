# Write A Python Program To Find Sum Of Two Number (1st Number Should Be Positive And 2nd Number Should Be Negative And Less Than 50 And Greater Than 20)

def sum(a:int,b:int):
    if a<0 or b>0 or b<-50 or b>-20:
        return "invalid number"
    return a+b

a=20
b=-25
print(f"Sum of {a} and {b} is {sum(a,b)}")