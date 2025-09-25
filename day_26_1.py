'''
You are given N lines of CSS code. Your task is to extract and print all the valid hex color codes used in CSS properties.

A valid hex color code:

Starts with #.

Followed by either 3 or 6 hexadecimal characters (0 to 9, a to f, A to F).

Appears only in CSS property values (after :, ,, or whitespace).

Ignore any hex-like strings used as selectors (e.g., #idName before {).

Output Format
Print each valid hex color code on a separate line, in the order they appear.

'''

#Code

#Optimized Code

import re
pattern = re.compile(r'(?<=[:\s,])#[0-9a-fA-F]{3,6}\b')
N = int(input())
for i in range(N):
    s = input()
    newHex = re.findall(pattern,s)
    for f in newHex:
        print(f)