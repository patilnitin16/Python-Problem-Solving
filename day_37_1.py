'''
You are given a positive integer N.
Print a numerical triangle of height N−1, as shown below.

Each line i (where 1 ≤ i < N) should contain the number i repeated i times.
You must not use strings — only arithmetic operations, a single for loop, and a single print statement.
'''

#Code

for i in range(1,int(input())):
    print(i * ((10**i)-1)//9)
    