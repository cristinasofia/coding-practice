# 673 https://leetcode.com/problems/number-of-longest-increasing-subsequence/

def findNumberOfLIS(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    
    if n <= 1:
        return n
    
    dp = [1] * n
    lengths = [1] * n
    max_ans = 1
    
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                #dp[i] = max(dp[i], dp[j] + 1)
                if dp[i] < dp[j] + 1:
                    dp[i] = 1 + dp[j]
                    lengths[i] = lengths[j]
                elif dp[i] == dp[j] + 1:
                    lengths[i] += lengths[j]
        
        max_ans = max(max_ans, dp[i])
        
    max_len = 0
    for x, y in zip(dp, lengths):
        if x == max_ans:
            max_len += y
    
    return max_len