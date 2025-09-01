'''
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2  
Function Description

Complete the swap_case function in the editor below.

swap_case has the following parameters:

string s: the string to modify
Returns

string: the modified string

'''



#Code

#Optimized MEthod
def swap_case(s):
    return "".join(
        letter.upper() if letter.islower() else letter.lower() 
        for letter in s
    )

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)




#BruteForce Method
def swap_case(s):
    newStr = ""
    for letter in s:
        if letter.islower():
            newStr+= letter.upper()
        else:
            newStr+=letter.lower()
    return newStr

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)