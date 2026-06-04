# Write A Python Program To Make A English Dictionary App That Translate Into Arabic
arabic_dict = {
    "hello": "مرحبا",
    "book": "كتاب",
    "pen": "قلم",
    "school": "مدرسة",
    "student": "طالب",
    "teacher": "معلم",
    "computer": "حاسوب",
    "water": "ماء",
    "food": "طعام",
    "house": "بيت"
}

word = input("Enter an English word: ").lower()

if word in arabic_dict:
    print("Arabic Translation:", arabic_dict[word])
else:
    print("Word not found in dictionary.")

