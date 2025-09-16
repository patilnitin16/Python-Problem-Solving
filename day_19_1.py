'''
You are given a string S.
Your task is to find out whether S is a valid regex or not.
Input Format
The first line contains integer T, the number of test cases.
The next T lines contains the string S.
Constraints
0<T<100
Output Format
Print "True" or "False" for each test case without quotes.

'''

#Code

import re 
def regexCheck(regex):
    try:
        if re.search(r'(\*|\+|\?){2,}', regex):
            return False
        else:
            re.compile(regex)
            return True
    except re.error:
        return False

N = int(input())
for _ in range(N):
    s = input()
    print(regexCheck(s))