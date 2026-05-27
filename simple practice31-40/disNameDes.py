# Write A Python Program To Get 10 Name Of The Students From The User In A List, Display That Students Name In Descending Order

names=[input("enter names one by one:") for i in range(10)]
names.sort()
print(names)
