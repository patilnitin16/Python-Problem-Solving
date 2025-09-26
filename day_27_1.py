'''
Write a program that validates a User ID (UID) based on the following criteria:
The UID must be exactly 10 characters long.
It must contain only alphanumeric characters (A-Z, a-z, 0-9).
It must contain at least 2 uppercase English alphabets.
It must contain at least 3 digits.
No character should repeat within the UID.

For each input UID, print "Valid" if it meets all the conditions, otherwise print "Invalid".

You will be given T
T test cases, each containing a UID string.

'''

#Code

import re 
pattern = re.compile(r'^(?=[A-Za-z0-9]{10}$)(?=(?:.*[A-Z]){2,})(?=(?:.*\d){3,})[A-Za-z0-9]{10}$')
T = int(input())
for _ in range(T):
    uid = input()
    if (len(set(uid)) == 10):
        ans = bool(pattern.fullmatch(uid))
        if(ans):
            print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")