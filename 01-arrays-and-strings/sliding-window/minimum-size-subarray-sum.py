# 209 https://leetcode.com/problems/minimum-size-subarray-sum/


def minSubArrayLen(s, nums):
    """
    :type s: int
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    
    i, j = 0, 0
    curr_sum = 0
    min_len = float("inf")
    
    while j < len(nums):
        curr_sum += nums[j]
        j += 1
        while curr_sum >= s:
            min_len = min(min_len, j - i)
            curr_sum -= nums[i]
            i += 1
    
    return min_len if min_len != float("inf") else 0