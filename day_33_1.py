'''
You are given a 2-dimensional matrix of size N × M.
Your task is to first find the minimum value in each row of the matrix, and then print the maximum value among those row minimums.


Input Format
The first line contains two integers N and M, the number of rows and columns.
The next N lines each contain M integers, representing the elements of the matrix.


Output Format
Print a single integer — the maximum among all row-wise minimum values.
'''

#Code

import numpy

N,M = map(int,input().split())
arrayA = [list(map(int,input().split())) for _ in range(N)]
print(numpy.max(numpy.min(arrayA,axis=1)))
