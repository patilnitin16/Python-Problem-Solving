'''
Write a Python function to determine whether two given strings are anagrams of each other.

Two strings are called anagrams if they contain the same characters in the same frequency but may appear in a different order.

Your function should return True if the two strings are anagrams of each other, otherwise return False.
'''

#Code
#Optimized Code
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        charCount = {}
        for ch in s:
            charCount[ch] = charCount.get(ch, 0) + 1
        for ch in t:
            charCount[ch] = charCount.get(ch, 0) - 1
        for value in charCount.values():
            if value != 0:
                return False
        return True

#BruteForce
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(list(map(str,s))) == sorted(list(map(str,t)))