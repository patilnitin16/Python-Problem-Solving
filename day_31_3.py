'''
Task

Your task is to print an array of size N X M with its main diagonal elements as 0's and 1's everywhere else.

'''

#code

#Optimized Code

import numpy
numpy.set_printoptions(legacy='1.13')

N,M = map(int,input().split())
print(numpy.eye(N,M))