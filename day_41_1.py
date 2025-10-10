'''
You are given a matrix of size N × M.
Each row contains M space-separated integers.
You are also given an integer K, representing the column index (0-based).

Your task is to sort the rows of the matrix in ascending order based on the values in the K-th column, and then print the resulting matrix.

'''

#Code


import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    for elem in sorted(arr,key=lambda x:x[k]):
        print(" ".join(map(str,elem)))