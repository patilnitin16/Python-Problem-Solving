'''
Task

You are given a string s.
Your task is to print all possible size k replacement combinations of the string in lexicographic sorted order.

Input Format

A single line containing the string  and integer value  separated by a space.

Constraints

The string contains only UPPERCASE characters.

Output Format

Print the combinations with their replacements of string s on separate lines.

'''

#Code

#Optimized Code

from itertools import combinations_with_replacement
s,k = input().split(" ")
for n in combinations_with_replacement(sorted(s),int(k)):
    print("".join(n))