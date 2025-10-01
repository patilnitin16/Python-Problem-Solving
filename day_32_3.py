'''
Write a Python program using NumPy that performs the following operations:

Read two integers N and M, where N is the number of rows and M is the number of columns in a matrix.

Read an N × M integer matrix as input.

Compute the sum of the elements along each column (axis = 0).

Compute the product of all the column sums.

Print the final result.
'''

#Code

#Optimized Code
import numpy

arrayA = []
N,M = map(int,input().split())
[arrayA.append(list(map(int,input().split()))) for _ in range(N)]
res = numpy.sum(arrayA,axis=0)
print(numpy.prod(res))



#BruteForce Code
import numpy

arrayA = []
N,M = map(int,input().split())
for _ in range(N):
    arrayA.append(list(map(int,input().split())))
res = numpy.sum(arrayA,axis=0)
print(numpy.prod(res))
