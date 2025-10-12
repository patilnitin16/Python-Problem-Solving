'''
Write a Python program to determine whether a series of credit card numbers are valid or invalid based on the following rules:

A valid credit card number must:
Start with a 4, 5, or 6.
Contain exactly 16 digits.
May have digits separated by single hyphens (-), e.g. 4123-4567-8912-3456.
Must consist of only digits and optional hyphens (no spaces or other symbols).
Must not have four or more consecutive repeated digits (like 1111 or 7777).

The program should take an integer N as input — the number of credit card numbers to check.

For each of the N credit card numbers, print:

"Valid" if the card number meets all the above conditions.

"Invalid" otherwise.
'''

#Code

import re
pattern = r"^(?!.*(\d)(-?\1){3})[4-6]\d{3}(-?\d{4}){3}$"
N = int(input())
for _ in range(N):
    print("Valid" if bool(re.match(pattern,input())) else "Invalid")