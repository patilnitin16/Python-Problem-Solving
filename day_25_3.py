'''
You are given a string N.
Your task is to verify that N is a floating point number.

In this task, a valid float number must satisfy all of the following requirements:

Number can start with +, - or . symbol.
For example:
✔ +4.50
✔ -1.0
✔ .5
✔ -.7
✔ +.4
✖ -+4.5
Number must contain at least  decimal value.
For example:
✖ 12.
✔ 12.0  

'''

#Code

#Optimized Code

import re
pattern = re.compile(r'^[\+\-]?(\d*\.\d+|\d+\.\d*)$')
T = int(input())
for i in range(T):
    str1 = input()
    print(bool(re.match(pattern,str1)))
