'''
Write a Python function lengthOfLastWord that takes a string s consisting of words and spaces, and returns the length of the last word in the string.

A word is defined as a sequence of non-space characters. The string may contain leading or trailing spaces, but they should be ignored.
'''

#code

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        newlst = s.split()
        return len(newlst[-1])