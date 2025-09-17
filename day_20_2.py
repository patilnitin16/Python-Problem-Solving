'''
Task : 

The National University conducts an examination of N students in X subjects.
Your task is to compute the average scores of each student.


Input Format
The first line contains N and X separated by a space.
The next X lines contains the space separated marks obtained by students in a particular subject.

'''

#Code

N,X = map(int,input().split())
finalSet = []
for i in range(X):
    newLst = list(map(float,input().split()))
    finalSet.append(newLst)
for student in zip(*finalSet):
    print(f"{sum(student)/X:.1f}")