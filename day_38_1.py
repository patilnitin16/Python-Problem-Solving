'''
Question:

Write a Python program that reads a string of digits and prints a list of tuples, where each tuple contains the count of consecutive occurrences of a digit and the digit itself.
You must use the itertools.groupby() function to group consecutive identical digits.

📥 Input Format:
A single line containing a string of digits.

📤 Output Format:
Print the list of tuples in the format:

(count, digit)

All tuples should be printed on one line separated by spaces.

'''

#code

import itertools

S = input()
for key,nums in itertools.groupby(S):
    print((sum(1 for _ in nums),int(key)),end=" ")