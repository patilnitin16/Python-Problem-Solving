'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
'''

#Code
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            for i in range(len(nums)-1):
                if nums[i] < target < nums[i+1]:
                    return i+1
            if nums[-1] < target:
                return len(nums)
            elif target < nums[0]:
                return 0
        
