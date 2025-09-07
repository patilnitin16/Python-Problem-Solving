'''


'''

#Code

#Optimized

K = int(input())
roomList = list(map(int,input().split(" ")))
orderedList = {}
for r in roomList:
    if r in orderedList:
        orderedList[r] += 1
    else:
        orderedList[r] = 1
for key,val in orderedList.items():
    if val == 1:
        print(key)




#BruteForce Method
n = int(input())
roomList = list(map(int,input().split(" ")))
captainRoom = 0
for i in range(len(roomList)):
    count = 0
    for j in range(len(roomList)):
        if roomList[j] == roomList[i]:
            count+=1
    if count == 1:
        captainRoom = roomList[i]
print(captainRoom)