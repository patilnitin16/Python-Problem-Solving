'''
Problem Statement

You are given a list of N lowercase English letters.
You need to randomly select K letters from this list (without considering the order of selection).
Your task is to find the probability that the selected group of K letters contains at least one letter 'a'.

Input Format
The first line contains an integer N, the number of letters in the list.
The second line contains N space-separated lowercase English letters.
The third line contains an integer K, the number of letters to be selected.

'''

#code

from itertools import combinations

N = int(input())
elements = list(input().split())
K = int(input())

coll = combinations(elements,K)
contains = 0
total = 0
for elem in coll:
    total+=1
    if "a" in elem:
        contains+=1
print(contains/total)