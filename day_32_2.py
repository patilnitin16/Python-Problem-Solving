'''
Write a Python program using NumPy that reads a list of floating-point numbers as input and performs the following operations:

Print the floor value of each number (largest integer less than or equal to the number).

Print the ceiling value of each number (smallest integer greater than or equal to the number).

Print the rounded value of each number to the nearest integer.

Use NumPy functions floor(), ceil(), and rint() for these operations.


'''

#Code

import numpy
numpy.set_printoptions(legacy="1.13")
A = list(map(float,input().split()))
print(numpy.floor(A))
print(numpy.ceil(A))
print(numpy.rint(A))