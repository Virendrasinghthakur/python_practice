# Write a Python Program to write data to excel cell using python xlsxwriter.

import xlsxwriter as xl

wb=xl.Workbook("n_sample.xlsx")
ws=wb.add_worksheet()

ws.write("A1","hii")

