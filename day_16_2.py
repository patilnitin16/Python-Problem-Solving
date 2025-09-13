'''
Task : You are the manager of a supermarket.
You have a list of  items together with their prices that consumers bought on a particular day.
Your task is to print each item_name and net_price in order of its first occurrence.
item_name = Name of the item.
net_price = Quantity of the item sold multiplied by the price of each item.

'''

#Code

#Optimized Code

from collections import OrderedDict
N = int(input())
ordered_list = OrderedDict()
for i in range(N):
    name = input().rsplit(" ",1)
    if name[0] in ordered_list:
        ordered_list[name[0]] += int(name[1])
    else:
        ordered_list[name[0]] = int(name[1])
for items,total in ordered_list.items():
    print(items,total)