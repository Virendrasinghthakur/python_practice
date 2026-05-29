# Write a Python Program to read specific column data from excel.

import openpyxl as ox

wb = ox.load_workbook("new.xlsx")
ws = wb.active

for cell in ws["A"]:
    print(cell.value)