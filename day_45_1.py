'''
You are given two integers, K and M. After that, you will receive K lists of integers. Each list begins with an integer Nᵢ, which represents the number of elements in that list, followed by Nᵢ space-separated integers. Your task is to pick exactly one element from each list in such a way that the value of the following expression is maximized:

S=(x1 ​+ x2 ​+ x3​ ) % M

where xᵢ denotes the element chosen from the iᵗʰ list, and % denotes the modulo operator. You need to calculate and print the maximum possible value of S that can be obtained.
'''

#Code

from itertools import product

K,M = map(int,input().split())
lists  = []

for i in range(K):
    arr = list(map(int,input().split()))[1:]
    lists.append(arr)
maxValue = 0
for combinations in product(*lists):
    value = sum(x**2 for x in combinations)%M
    maxValue = max(maxValue,value)
print(maxValue)