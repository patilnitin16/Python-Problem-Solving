'''Concept : A valid mobile number is a ten digit number starting with a 7,8 or 9.
Regular expressions are a key concept in any programming language. A quick explanation with Python examples is available here. You could also go through the link below to read more about regular expressions in Python.'''

#Code

#Optimized code
import re
pattern = re.compile(r'^[789]\d{9}$')
N = int(input())
for _ in range(N):
    newNum = input().strip()
    if pattern.match(newNum):
        print("YES")
    else:
        print("NO")

#BruteForce Method
import re
N = int(input())
for i in range(N):
    newNum = input()
    if len(newNum) == 10 and not re.search(r'[a-zA-Z]', newNum):
        if(newNum[0] == "7") or (newNum[0] == "8") or (newNum[0] == "9"):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
