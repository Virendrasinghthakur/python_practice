# Write a Python Program to Create a excel file using python using xlswriter library

import xlsxwriter

workbook=xlsxwriter.Workbook('sample.xlsx')

worksheet=workbook.add_worksheet()

worksheet.write('A1','Name')
worksheet.write('A2','Marks')

worksheet.write('A2', 'Virendra')
worksheet.write('B2', 95)

worksheet.write('A3', 'Rahul')
worksheet.write('B3', 88)

workbook.close()

print("excel file created succesfully")

