# Write A Python Program To Create A CSV File To Store Odd Number As Generated From 200 To 100.

import csv
c="sample.csv"


odd=[i for i in range(200,100,-1) if not i%2]
print(odd)
with open(c,"w",newline="") as f:
    writer=csv.writer(f)

    for num in odd:
        writer.writerow([num])