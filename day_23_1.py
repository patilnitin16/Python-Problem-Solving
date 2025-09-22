'''
Task
You are given a space separated list of integers . If all the integers are positive, then you need to check if any integer is a palindromic integer.

Output Format

Print True if all the conditions of the problem statement are satisfied. Otherwise, print False.

'''

#Code

#Optimized Code
N = int(input())
newList = list(map(int,input().split()))
if any(num >=0 for num in newList) and any(str(num) == str(num)[::-1] for num in newList):
    print(True)
else:
    print(False)


#BruteForce Method
N = int(input())
newList = list(map(int,input().split()))
if all(num >= 0 for num in newList):
    found = False
    for num in newList:
        if str(num) == str(num)[::-1]:
            print(True)
            found = True
            break
    if not found:
        print(False)
else:
    print(False)   