'''
You are given an array of integers nums and an integer target. Your task is to find the indices of the two numbers in the array that add up to the given target.

You may assume that each input would have exactly one solution, and you cannot use the same element twice. Return the indices of the two numbers in the form of a list [index1, index2].

Write a Python class Solution with a method twoSum(self, nums, target) that takes the list of numbers and the target value as input and returns the indices of the two numbers whose sum equals the target.
'''

#Code

#Optimized Code
class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i,num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement],i]
            seen[num] = i


#BruteForce Method
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] + nums[i] == target:
                    return [i,j]