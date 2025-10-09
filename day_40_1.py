'''
You are given several test cases.
For each test case, you have a row of cubes (blocks) of different side lengths.
Your task is to determine whether it is possible to stack all the cubes into one pile following these rules:

You can pick up cubes only from either end of the row (leftmost or rightmost).

When placing a cube on the pile, its side length must be less than or equal to the cube that is already on top of the pile.

In other words, the pile must be built in non-increasing order (each cube smaller than or equal to the previous one).

You must use all the cubes to build the pile.

If it is possible to build such a pile, print "Yes", otherwise print "No".
'''

#Code

from collections import deque
T = int(input())
for i in range(T):
    n = int(input())
    dq = deque(list(map(int,input().split())))
    last = float("inf")
    pillePossible = True
    while dq:
        if dq[0] > dq[-1]:
            pick = dq.popleft()
        else:
            pick = dq.pop()
        if pick <= last:
            last = pick
        else:
            pillePossible = False
            break
    print("Yes" if pillePossible else "No")