'''
Write a Python function removeElement that removes all occurrences of a specified value from a given list in place (without creating a new list).

The function should iterate through the list and delete every element equal to a given value val. After removing all such elements, it should return the new length of the modified list.
'''
#Code

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.remove(nums[i])
            else:
                i+=1
        return len(nums)