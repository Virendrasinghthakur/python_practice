# Write a Python program to create a nested TUPLE.



n=int(input("enter the numer of tuple to be nested:"))

main=tuple()
for i in range(n):
    t=tuple(map(int,input("enter the elements of the tuple :").split()))
    main+=(t,)
print(main)
