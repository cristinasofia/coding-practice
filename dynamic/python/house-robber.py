#198 https://leetcode.com/problems/house-robber/
def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    if n == 0:
        return n
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])
    
    dp = [0 for _ in range(n)]
    dp[0] = nums[0]
    dp[1] = nums[1]
    
    for i in range(2, n):
        prev = dp[i-2]
        dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        dp[i-1] = max(dp[i-1], prev)
    
    
    return dp[n-1]