# Write a Python Numpy Program to access one particular value of a matrix

import numpy as np

matrix = np.array([[10, 20, 30],
                   [40, 50, 60],
                   [70, 80, 90]])

value = matrix[1, 2]

print("Particular value:", value)
