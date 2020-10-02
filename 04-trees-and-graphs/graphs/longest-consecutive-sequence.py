# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max_len = 0
        nums = set(nums) # conversion is O(n), purpose of set is to find a number in O(1) time
        
        for x in nums:
            if x - 1 not in nums:   # if x = 0 is not in nums
                y = x + 1           # y = 1
                while y in nums:    # y = 2, 3, 4
                    y += 1          
                max_len = max(max_len, y - x) # 4 - 0 
        return max_len