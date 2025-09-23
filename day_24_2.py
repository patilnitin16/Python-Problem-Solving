'''
Task
You are given a string s.
Your task is to find the indices of the start and end of string s in k.

Input Format

The first line contains the string s.
The second line contains the string k.

Output Format

Print the tuple in this format: (start _index, end _index).
If no match is found, print (-1, -1).

'''

#Code

#Optimized Code

import re
s = input()
k = input()
pattern = f"(?=({k}))"
matches = list(re.finditer(pattern,s))
if matches:
    for m in matches:
        print((m.start(),(m.start() + len(k) - 1)))
else:
    print((-1,-1))