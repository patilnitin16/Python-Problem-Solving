'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''

#Code

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {")":"(","}":"{","]":"["}
        for ch in s:
            if ch in matching:
                topElement = stack.pop() if stack else "#"
                if matching[ch] != topElement:
                    return False
            else:
                stack.append(ch)
        return not stack