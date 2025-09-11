'''
Task

You are given a string .
Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.

Input Format

A single line containing the string s and integer value k separated by a space.

The string contains only UPPERCASE characters.

Output Format

Print the different combinations of string  on separate lines.

'''

#Code

#Optimized Code

from itertools import combinations
s,k = input().split(" ")
for i in range(1,int(k)+1):
    for n in combinations(sorted(s),i):
        print("".join(n))