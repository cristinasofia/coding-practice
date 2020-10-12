#128 https://leetcode.com/problems/longest-consecutive-sequence/

def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    max_len = 0
    nums = set(nums) # conversion is O(n), purpose of set is to find a number in O(1) time
    
    while nums:
        n = nums.pop()
        i = n - 1
        while i in nums:
            nums.remove(i)
            i -= 1
        j = n + 1
        while j in nums:
            nums.remove(j)
            j += 1
            
        max_len = max(max_len, j - i - 1)
        
    return max_len