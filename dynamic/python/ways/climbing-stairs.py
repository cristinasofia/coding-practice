# 70 https://leetcode.com/problems/climbing-stairs/

def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    
    if n <= 1:
        return n
    
    dp = [0 for _ in range(n+1)]
    ways = [1,2]
    
    dp[0] = 1
    
    for i in range(1, n+1):
        for j in range(len(ways)):
            dp[i] = dp[i - ways[j]] + dp[i]

    return dp[n]