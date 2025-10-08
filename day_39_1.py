'''
Write a Python program that reads a number N, followed by N strings, and performs the following tasks:

Count how many distinct strings are entered.

Print the total number of distinct strings.

Print how many times each string appeared, in the order they were first entered.

Use the collections.Counter class to perform the counting efficiently.

'''

#Code

import collections
n = int(input())
arrayA = []
for _ in range(n):
    arrayA.append(input())
newCount = collections.Counter(arrayA)
print(len(newCount))
for i in newCount.values():
    print(i,end=" ")