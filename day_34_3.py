'''
Write a Python program using NumPy to compute the determinant of a square matrix.

First, take an integer 
𝑁
N as input, representing the order of the matrix.

Then, take 
𝑁
N rows of input containing 
𝑁
N floating-point numbers each.

Use numpy.linalg.det() to find the determinant of the matrix.

Print the result rounded to 2 decimal places.

'''

#Code

import numpy

N = int(input())
arrayA = numpy.array([list(map(float,input().split())) for _ in range(N)])
print(round(numpy.linalg.det(arrayA),2))