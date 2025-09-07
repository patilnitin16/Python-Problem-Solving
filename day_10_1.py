'''
Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.
One fine day, a finite number of tourists come to stay at the hotel.
The tourists consist of:
→ A Captain.
→ An unknown group of families consisting of  members per group where  ≠ .
The Captain was given a separate room, and the rest were given one room per group.
Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of the tourists. The room numbers will appear  times per group except for the Captain's room.
Mr. Anant needs you to help him find the Captain's room number.
The total number of tourists or the total number of groups of families is not known to you.
You only know the value of  and the room number list.
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