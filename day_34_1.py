'''

Question:
Write a Python program using NumPy that takes two 1-D integer arrays as input. First, compute and print their inner product, then compute and print their outer product.

'''

#Code

import numpy

arrayA = numpy.array(list(map(int,input().split())))
arrayB = numpy.array(list(map(int,input().split())))
print(numpy.inner(arrayA,arrayB))
print(numpy.outer(arrayA,arrayB))
