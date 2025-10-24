'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
'''

#Code

class Solution:
    def romanToInt(self, s: str) -> int:
        newDict = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        newInt = 0
        for i in range(len(s)):
            if i+1 < len(s) and newDict[s[i]] < newDict[s[i+1]]:
                newInt -= newDict[s[i]]
            else:
                newInt += newDict[s[i]]
        return newInt