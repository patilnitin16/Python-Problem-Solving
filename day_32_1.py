'''
Write a Python program using NumPy that reads two integer matrices A and B of size N × M from user input and performs the following operations:

Element-wise addition of A and B.

Element-wise subtraction of A and B.

Element-wise multiplication of A and B.

Element-wise floor division of A by B.

Element-wise modulus of A by B.

Element-wise power operation where each element of A is raised to the power of the corresponding element in B.

Finally, print the result of each operation on a new line.
'''

#Code

import numpy

N,M = map(int,input().split())
arrayA = []
arrayB = []
[arrayA.append(list(map(int,input().split()))) for _ in range(N)]
[arrayB.append(list(map(int,input().split()))) for _ in range(N)]
print(numpy.add(arrayA,arrayB))
print(numpy.subtract(arrayA,arrayB))
print(numpy.multiply(arrayA,arrayB))
print(numpy.floor_divide(arrayA,arrayB))
print(numpy.mod(arrayA,arrayB))
print(numpy.power(arrayA,arrayB))
