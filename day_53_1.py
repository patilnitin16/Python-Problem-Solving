'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
'''

#Code
#Optimized code
def missingNumber(nums):
        n = len(nums)
        expectedSum = n * (n+1) // 2
        actualSum = sum(nums)
        return expectedSum - actualSum


#BruteForce
def missingNumber(nums):
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i:
                return i

