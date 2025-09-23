'''
Task

You are given a string s.
Your task is to find the first occurrence of an alphanumeric character in  (read from left to right) that has consecutive repetitions.

Input Format

A single line of input containing the string S.

Output Format

Print the first occurrence of the repeating character. If there are no repeating characters, print -1.

'''

#Code

#Optimized Code

import re
s = input()
matches = re.search(r"([a-zA-Z0-9])\1",s)
if matches:
    print(matches.group(1))
else:
    print(-1)
