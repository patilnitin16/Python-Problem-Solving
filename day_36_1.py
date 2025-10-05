'''
You are given an array of integers and two sets, A and B.
Your task is to find the happiness score of the array.

You gain +1 happiness for each element of the array that is present in set A.

You lose -1 happiness for each element of the array that is present in set B.

Elements not present in either set do not affect happiness.

Print the final happiness score.

'''

#code

n,m = map(int,input().split())
arrayA = list(map(int,input().split()))
setA = set(map(int,input().split()))
setB = set(map(int,input().split()))
happiness = 0
for num in arrayA:
    if num in setA:
        happiness+=1
    elif num in setB:
        happiness-=1
print(happiness)