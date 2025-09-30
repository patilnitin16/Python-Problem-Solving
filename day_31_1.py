'''
You are given two integer matrices of dimensions N × P and M × P.
Your task is to read both matrices and then concatenate them along the rows (axis = 0). Finally, print the resulting matrix.
Input Format:
The first line contains three space-separated integers:
N, M, P
where:
N → number of rows in the first matrix
M → number of rows in the second matrix
P → number of columns in each matrix
The next N lines each contain P integers describing the first matrix.
The following M lines each contain P integers describing the second matrix.
'''
#Code

#Optimized Code
import numpy
N,M,P = map(int,input().split())
array1 = numpy.array([list(map(int,input().split())) for _ in range(N)])
array2 = numpy.array([list(map(int,input().split())) for _ in range(M)])

print(numpy.concatenate((array1,array2),axis = 0))

#BruteForce Code
import numpy
array1 = []
array2 = []
N,M,P = map(int,input().split())
for i in range(N):
    newLst = list(map(int,input().split()))
    array1.append(newLst)
for i in range(M):
    newLst = list(map(int,input().split()))
    array2.append(newLst)
print(numpy.concatenate((numpy.array(array1),numpy.array(array2)),axis = 0))