'''
Task
You are given a complex . Your task is to convert it to polar coordinates.

Input Format

A single line containing the complex number . Note: complex() function can be used in python to convert the input as a complex number.

Constraints

Given number is a valid complex number

Output Format

Output two lines:
The first line should contain the value of r.
The second line should contain the value of Phi.

'''

#Code 

#Optimized Code

import cmath
complexNum = complex(input())
print(abs(complexNum))
print(cmath.phase(complexNum))