'''
Dr. John Wesley has a spreadsheet containing a list of student's IDs, marks, class and name.
Your task is to help Dr. Wesley calculate the average marks of the students.
Average = Sum of all marks Total Students
Note:
1. Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet.
2. Column names are ID, MARKS, CLASS and NAME. (The spelling and case type of these names won't change.)

Output Format
Print the average marks of the list corrected to 2 decimal places.

'''

#Code

#Optimized Code
from collections import namedtuple
N = int(input())
columns = input().split()
student = namedtuple("student",columns)
data  = [student(*input().split()) for i in range(N)]
avg = sum(int(s.MARKS) for s in data)/N
print(format(avg,".2f"))

#BruteForce Code
from collections import namedtuple
N = int(input())
columns = input().split()
student = namedtuple("student",columns)
data  = [student(*input().split()) for i in range(N)]
avg = 0
for item in data:
      avg += int(item.MARKS)
print(format((avg/N),".2f"))