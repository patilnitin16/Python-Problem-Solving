'''

In this challenge, you will be given 2 integers, n and m. There are n words, which might repeat, in word group A. There are  words belonging to word group B. For each m words, check whether the word has appeared in group A or not. Print the indices of each occurrence of m in group A. If it does not appear, print -1.

'''

#Code

#Optimized Code

from collections import defaultdict
n,m = input().split(" ")
positions = defaultdict(list)
for i in range(1,int(n)+1):
    word = input()
    positions[word].append(i)
for j in range(int(m)):
    word = input()
    if word in positions:
        print(" ".join(map(str,positions[word])))
    else:
        print(-1)