# write a program to check alpha character wether vowel or cons. and also display it is number ,user give any number.

s=input("enter your character :")
if s.lower() in ("a","e","i","o","u"):
    print(f"your char {s} is a vowel ")
elif s.lower()<'a':
    print(f"you enter a number")
else:
    print(f"youe char {s} is a consonant ")