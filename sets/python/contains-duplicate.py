# 217 https://leetcode.com/problems/contains-duplicate/

"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, 
and it should return false if every element is distinct.
"""

def containsDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    
    return len(set(nums)) != len(nums)

# list to set: set(nums) is O(n)
# if len(set) != len(nums), then there are duplicates and the statement is True