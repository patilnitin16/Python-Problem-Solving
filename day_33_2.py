'''
You are given a matrix of size N × M.
Your task is to perform the following operations using NumPy:

Compute the mean of each row.

Compute the variance of each column.

Compute the standard deviation of the entire matrix, rounded to 11 decimal places.

Input Format
The first line contains two integers N and M, the number of rows and columns.
The next N lines each contain M integers, representing the elements of the matrix.

Output Format
First line: A NumPy array containing the mean of each row.
Second line: A NumPy array containing the variance of each column.
Third line: A floating-point number representing the standard deviation of the entire matrix, rounded to 11 decimal places.
'''

#Code

import numpy

N,M = map(int,input().split())
arrayA = [list(map(int,input().split())) for _ in range(N)]
print(numpy.mean(arrayA,axis=1))
print(numpy.var(arrayA,axis=0))
print(round(numpy.std(arrayA),11))
