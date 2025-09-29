'''
Task

You are given a N X M integer array matrix with space separated elements ( = rows and  = columns).
Your task is to print the transpose and flatten results.

'''

#Code

#Optimized Code
import numpy as np

N, M = map(int, input().split())
arr = np.array([list(map(int, input().split())) for _ in range(N)])

print(arr.T)          
print(arr.flatten()) 


#BruteForce Code
import numpy

N,M = input().split()
newMetrix = []
for i in range(int(N)):
    rows = list(map(int,input().split()))
    newMetrix.append(rows)
newArray = numpy.array(newMetrix)
print(numpy.transpose(newArray))
print(newArray.flatten())

