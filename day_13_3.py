'''
Task

You are given a string s.
Your task is to print all possible permutations of size k of the string in lexicographic sorted order.

Input Format

A single line containing the space separated string s and the integer value .

'''

#Code

#Optimized Code

from itertools import permutations
s,k = input().split(" ")
for p in permutations(sorted(s),int(k)):
    print("".join(p))


#Brute Force

from itertools import permutations 
s,k = input().split(" ") 
c = list(permutations(s,int(k))) 
c.sort() 
for n in c:
    print("".join(n))