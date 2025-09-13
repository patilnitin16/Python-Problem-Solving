'''   Task : Perform append, pop, popleft and appendleft methods on an empty deque .
The first line contains an integer , the number of operations.
The next  lines contains the space separated names of methods and their values.
Output Format : Print the space separated elements of deque .'''

#Code

#Optimized Code

from collections import deque
N = int(input())
d = deque()
for i in range(N):
    cmd, *args = input().split()
    if cmd == "append":
        d.append(args[0])
    elif cmd == "appendleft":
        d.appendleft(args[0])
    elif cmd == "clear":
        d.clear()
    elif cmd == "extend":
        d.extend(args)
    elif cmd == "extendleft":
        d.extendleft(args)
    elif cmd == "count":
        d.count(args[0])
    elif cmd == "pop":
        d.pop()
    elif cmd == "popleft":
        d.popleft()
    elif cmd == "remove":
        d.remove(args[0])
    elif cmd == "reverse":
        d.reverse()
    elif cmd == "rotate":
        d.rotate(args[0])
print(*d)