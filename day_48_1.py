'''
Write a Python program that determines whether a given integer is a palindrome or not.

A palindrome number is a number that reads the same backward as forward.
For example, 121 is a palindrome because reversing it gives the same number 121,
but 123 is not a palindrome since reversing it gives 321.
'''

#Code
#1
class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if str(x) == str(x)[::-1]:
            return True
        return False

#2
class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        orig = x
        while x > 0:
            rem = x % 10
            rev = rev *10 + rem
            x = x//10
        return rev == orig