'''
Task

You are given a two lists  and . Your task is to compute their cartesian product X.

Example

A = [1, 2]
B = [3, 4]

AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]
Note: A and B are sorted lists, and the cartesian product's tuples should be output in sorted order.

'''

#Code

#Optimized Code

from itertools import product
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(product(A,B))
for n in C:
    print(n,end=" ")
