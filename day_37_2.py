'''
You are given an integer N.
Your task is to print a pattern where the i-th line (for 1 ≤ i ≤ N) displays the square of a number that consists of i repeated 1’s.

You must not use strings or string multiplication — only arithmetic operations.

'''

#Code

for i in range(1,int(input())+1):
    print((((10**i)-1)//9) * (((10**i)-1)//9))