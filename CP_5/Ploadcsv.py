# Write a Python program to load csv file using pandas and print the shape of the csv file and display data in the form of string.

import pandas as pd

file=pd.read_csv("sample.csv")
print(file)
print(file.shape)