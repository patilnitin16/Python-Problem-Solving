'''
Write a Python program that takes a Postal Index Number (PIN code) as input and determines whether it is a valid Indian PIN code based on the following rules:

A valid PIN code must be a 6-digit number.
The PIN code cannot start with 0.
The PIN code must not contain more than one alternating repetitive digit pair.

An alternating repetitive digit pair is a digit that repeats with exactly one digit between them.
Example of such a pair: 121, 343, 565, etc.
Example: In the PIN 121426, the pattern 121 forms one such pair.

The program should print True if the PIN code is valid, otherwise False.

'''

#Code

regex_integer_in_range = r"^[1-9][0-9]{5}$"
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"


import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)