# Write a Python program to read an excel file using other than xlwings

import openpyxl as ox

wb=ox.Workbook()
ws=wb.active
ws["A1"]="hii"
wb.save("new.xlsx")
