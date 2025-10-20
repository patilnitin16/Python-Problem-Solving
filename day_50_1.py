'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
'''
#Code

#optimized code
class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x != 0:
            rev = rev * 10 + x % 10
            x //= 10
        rev *= sign
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return rev
#2
class Solution:
    def reverse(self, x: int) -> int:
        isnegative = False
        if x < 0:
            isnegative = True
            x = x * -1
        rev = 0
        while x > 0:
            rem = x % 10
            rev = rev * 10 + rem
            x = x//10
        if isnegative:
            rev = rev * -1
        if (rev < -2147483648 or rev > 2147483647):
            return 0
        return rev