'''
You are given a list of names paired with email addresses. Your task is to validate each email address according to the following rules and print only the valid name–email pairs.

Username must start with an English alphabet character (a to z or A to Z).

Subsequent characters may be alphanumeric, dot (.), underscore (_), or hyphen (-).

Domain must contain only English alphabets.

Extension must contain only English alphabets and must be 1 to 3 characters long.

Output Format:

Print only the valid name <email> pairs, one per line, in the order received.
'''

#Code

import re
import email.utils
pattern = re.compile(r'^[a-zA-Z][a-zA-Z0-9._-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$')
n = int(input())
for _ in range(n):
    newValue = email.utils.parseaddr(input())
    ans = bool(re.match(pattern,newValue[1]))
    if(ans):
        print(email.utils.formataddr(newValue))
        
