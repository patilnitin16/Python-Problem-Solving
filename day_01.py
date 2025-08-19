#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.


#Code

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    first = -100
    last = 0
    for i in range(n):
        if arr[i] > first:
            last = first
            first = arr[i]
    print(last)
    