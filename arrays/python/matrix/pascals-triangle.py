# 118 https://leetcode.com/problems/pascals-triangle/

def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    
    dp = [[1] * (i+1) for i in range(numRows)]
    
    for i in range(numRows):
        for j in range(1, i):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    
    return dp