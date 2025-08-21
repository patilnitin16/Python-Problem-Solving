'''
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

Input Format

The first line of input contains the original string. The next line contains the substring.

'''



#Code

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        character = string[i]
        for j in range(i+1,len(string)):
            character+=string[j]
            if character == sub_string:
                count+=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)