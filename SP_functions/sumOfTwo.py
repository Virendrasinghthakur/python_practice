# Write A Python Program To Find Sum Of Two Number (That Number Should Be Positive  And Less Than 50)

def sum(a:int,b:int):
    if (a or b) >50 or (a or b) < 0:
        return "invalid number"
    return a+b

a=-1
b=55
print(f"Sum of {a} and {b} is {sum(a,b)}")