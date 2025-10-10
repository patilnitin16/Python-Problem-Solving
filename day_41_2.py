'''
You are given a string S containing a mix of uppercase letters, lowercase letters, and digits.
Your task is to rearrange the characters of the string in the following order:
All lowercase letters (sorted alphabetically)
All uppercase letters (sorted alphabetically)
All odd digits (sorted in ascending order)
All even digits (sorted in ascending order)
Finally, print the resulting string.
'''
#Code

#Optimized Code
S = input()
lower,upper,even,odd = [],[],[],[]
for elem in S:
    if elem.isalpha():
        (upper if elem.isupper() else lower).append(elem)
    elif elem.isalnum():
        (even if int(elem) % 2 == 0 else odd).append(elem)
print("".join(sorted(lower)+ sorted(upper)+sorted(odd)+sorted(even)))

#Big Code
S = input() 
lower = "" 
upper = "" 
odd = "" 
even = "" 
for elem in S:
    if elem.isalpha(): 
        if elem.isupper():
             upper += elem 
        else: lower += elem 
    elif elem.isalnum(): 
        if int(elem) % 2 == 0:
             even += elem 
        else: odd += elem 
print("".join(map(str,(sorted(lower)+ sorted(upper)+sorted(odd)+sorted(even)))))