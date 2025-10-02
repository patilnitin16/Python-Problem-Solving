

'''
You are given two square matrices of size N × N.
Your task is to compute and print the dot product (matrix multiplication) of the two matrices using NumPy.

Input Format
The first line contains an integer N, the size of the matrices.
The next N lines each contain N integers representing the first matrix (arrayA).
The following N lines each contain N integers representing the second matrix (arrayB).

Output Format
Print the result of the dot product (arrayA × arrayB) as a NumPy 2D array.

'''

#Code

import numpy

N = int(input())
arrayA = [list(map(int,input().split())) for _ in range(N)]
arrayB = [list(map(int,input().split())) for _ in range(N)]
print(numpy.dot(arrayA,arrayB))