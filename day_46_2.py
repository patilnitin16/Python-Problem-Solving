'''
Write a Python program to reverse a given list of characters in place (without using any extra space).

You need to modify the list directly using the two pointer technique, where one pointer starts from the beginning and the other from the end of the list.

After reversing the list, print the updated list.
'''

#Code

class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s)-1
        while left < right:
            s[left],s[right] = s[right],s[left]
            left += 1
            right -= 1
        print(s)