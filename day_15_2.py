'''
Task

Raghu is a shoe shop owner. His shop has  number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are  number of customers who are willing to pay  amount of money only if they get the shoe of their desired size.

Your task is to compute how much money  earned.

'''


#Code

#Optimized Code

from collections import Counter
X = int(input())
shoes = Counter(list(map(int,input().split(" "))))
N = int(input())
earnings = 0
for i in range(N):
    a,b = input().split(" ")
    if shoes[int(a)] > 0:
        earnings += int(b)
        shoes[int(a)] -= 1
print(earnings)
    