# write a program to check alpha character ,whethr vowel or concsonants

s=input("enter your character :")
if s.lower() in ("a","e","i","o","u"):
    print(f"your char {s} is a vowel ")
else:
    print(f"youe char {s} is a consonant ")