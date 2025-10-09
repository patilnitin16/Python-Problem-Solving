'''
When users post updates on social media platforms, their posts are timestamped based on the time zone they are in. Sometimes, these posts are viewed by users in different time zones, making it necessary to calculate the exact time difference between when a post was made and when it was seen.

You are given two timestamps for each test case, representing the time a post was published and the time it was viewed, both including timezone information.

Your task is to calculate the absolute difference in seconds between these two timestamps.
'''

#Code

import math
import os
import random
import re
import sys
from datetime import datetime

def time_delta(t1, t2):
    time1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    time2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    diff = abs(int((time1-time2).total_seconds()))
    return diff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        fptr.write(delta + '\n')
    fptr.close()