'''
Task:
You are given a string S. It consists of alphanumeric characters, spaces, and symbols (+, -).
Your job is to find all substrings of S that:

Contain 2 or more vowels.
Appear between two consonants.
Contain only vowels inside the substring.

Output Format:

Print each matched substring (in order of occurrence) on a new line.
If no match exists, print -1.

'''

#Code

#Optimized Code

import re
pattern = re.compile(r'(?<=[^aeiouAEIOU])([aeiouAEIOU]{2,})(?=[^aeiouAEIOU])')
S = input()
matches = list(re.finditer(pattern,S))
if matches:
    for m in matches:
        print(m.group())
else:
    print(-1)