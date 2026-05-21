
# Grade calculator

score=int(input("enter your score :"))
if score<60:
    Grade="F"
elif score>60 and score <=69:
    Grade="D"
elif score>70 and score <=79:
    Grade="C"
elif score>80 and score <=89:
    Grade="B"
elif score>90 and score <=100:
    Grade="A"

print(f"You got {Grade} grade")