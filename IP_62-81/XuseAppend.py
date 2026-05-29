# Write a Python Program to use append method in excel using python

import xlsxwriter as xs

wb=xs.Workbook("sample.xlsx")
ws=wb.add_worksheet()


data = [
    ["Name", "Marks"],
    ["Virendra", 95],
    ["Rahul", 88],
    ["Amit", 90]
]


for row_num, row_data in enumerate(data):
    ws.write_row(row_num,0,row_data)

wb.close()