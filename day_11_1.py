'''
You are given a set A and n other sets.
Your job is to find whether set A is a strict superset of each of the N sets.

Print True, if A is a strict superset of each of the N sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset.

'''

#Code

#Optimized Code

setA = set(map(int,input().split(" ")))
n = int(input())
isTrue = True
for i in range(n):
    newSet = set(map(int,input().split(" ")))
    if not setA.issuperset(newSet) and setA != newSet:
        isTrue = False
print(isTrue)