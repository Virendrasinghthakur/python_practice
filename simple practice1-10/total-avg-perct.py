#  write a program to calculate the total, average, prcentage of 6 subjects and display them to user

marks=[85,89,65,96,68,87]

avg=sum(marks)/len(marks)
total=sum(marks)
per=sum(marks)/6

print(f" Your total marks for the marks {marks} are {total:.2f} average for them is {avg:.0f} and percentages are {per:.2f}%")

