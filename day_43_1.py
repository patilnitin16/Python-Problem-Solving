'''
Write a Python program that reads N lines of text and replaces all occurrences of the logical operators
&& with "and" and || with "or", but only when they are surrounded by spaces.

Use the re.sub() function from the re (regular expressions) module and apply lookaround assertions so that replacements happen only when && or || are separate tokens (i.e., surrounded by spaces).
'''

#Code

import re 
N = int(input())
for i in range(N):
    line = input()
    line = re.sub(r'(?<= )&&(?= )', 'and', line)
    line = re.sub(r'( \|\| )',' or ',line)
    print(line)