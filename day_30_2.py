'''
You are given a space separated list of nine integers. Your task is to convert this list into a 3 X 3 NumPy array.

Input Format

A single line of input containing 9 space separated integers.

Output Format

Print the X NumPy array.

Sample Input

1 2 3 4 5 6 7 8 9
Sample Output

[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''

#Code

import numpy

newArry = list(map(int,input().split()))
print(numpy.reshape(newArry,(3,3)))