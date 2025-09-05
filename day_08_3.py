'''
Task

Students of District College have a subscription to English and French newspapers. Some students have subscribed to only the English newspaper, some have subscribed to only the French newspaper, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to only English newspapers.

'''

#Code

#Optimized Method

n1 = int(input())
set1 = set(map(int,input().split(" ")))
n2 = int(input())
set2 = set(map(int,input().split(" ")))
print(len(set1.difference(set2)))