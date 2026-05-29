# Write a Python program to read an excel file using xlwings

import xlwings as xw

# wb=xw.Book()
# sheet=wb.sheets[0]

# sheet["A1"].value="Hello"
# sheet["A2"].value=[10,20,30,40]

# wb.save("sample.xlsx")

wb1=xw.Book("C:/Users/Asus/Downloads/products.csv")

sheet=wb1.sheets[0]

# value=sheet["A1:B5"].value
# print(value)

# value=sheet.range("A3").expand().value
# for row in value:
#     print(row)

data=sheet.used_range.value
print(data)