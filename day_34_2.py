'''
Write a Python program using NumPy that evaluates a polynomial at a given value of 
𝑥
x.

The program should take the coefficients of the polynomial as input (highest degree first).

Then, take a single integer value of 
𝑥
x.

Finally, use numpy.polyval() to calculate and print the value of the polynomial at that 
𝑥
x.

'''

#Code

import numpy

polyAraay = numpy.array(list(map(float,input().split())))
x = int(input())
print(numpy.polyval(polyAraay,x))