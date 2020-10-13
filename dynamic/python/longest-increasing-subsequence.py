# 300 https://leetcode.com/problems/longest-increasing-subsequence/

def lengthOfLIS(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    
    dp = [1]*len(nums)
    max_ans = 1
    
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
        
        max_ans = max(max_ans, dp[i])
        
    return max_ans