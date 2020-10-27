# 238 https://leetcode.com/problems/product-of-array-except-self/

def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    
    dp = [0] * len(nums)
    dp[0] = 1
    for i in range(1, len(nums)):
        dp[i] = dp[i-1] * nums[i-1]
        
    x = 1
    for i in reversed(range(len(nums))):
        dp[i] *= x
        x *= nums[i]
        
    return dp

# O(n^2) without division
def productExceptSelf2(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    
    n = len(nums)
    dp = [1 for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i != j:
                dp[j] *= nums[i]
    
    return dp

# with division
def productExceptSelf3(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    
    n = len(nums)
    dp = [1 for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            dp[j] *= nums[i]
        dp[i] /= nums[i]
    
    return dp