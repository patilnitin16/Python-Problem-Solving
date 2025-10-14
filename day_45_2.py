'''
Mr. Vincent works in a door mat manufacturing company. One day, he decided to design a new door mat with the following specifications:

The mat size must be N × M, where

N is an odd natural number, and

M is 3 times N.

The design should have the word ‘WELCOME’ written in the center.

The design pattern should only use the characters .|. and -.

'''

#Code

N,M = map(int,input().split())
for i in range(N//2):
    pattern = ".|."* (2 * i + 1)
    print(pattern.center(M,"-"))
print("WELCOME".center(M,"-"))
for i in range(N//2,0,-1):
    pattern = ".|."* (2 * i - 1)
    print(pattern.center(M,"-"))