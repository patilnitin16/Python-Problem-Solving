'''
A company wants to create a logo using the three most common characters from its company name.
Given a string s that represents the company name in lowercase letters, write a program to find and print the three most frequent characters in the string.

Requirements:

Print the three most common characters along with their occurrence count.

Sort the characters by:

Descending order of frequency, and

Alphabetical order if two characters have the same frequency.

Print each character and its count on a new line
'''

#Code

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()
    newCounts = Counter(s)
    sortedArray = sorted(newCounts.items(), key=lambda x: (-x[1],x[0]))
    for i in range(3):
        print(sortedArray[i][0],sortedArray[i][1])
    
