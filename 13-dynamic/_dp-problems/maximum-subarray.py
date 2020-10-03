
def maxSubarray(nums):
    dp = [0] * len(nums)
    dp[0] = nums[0]
    max_sum = dp[0]

    for i in range(1, len(nums)):
        dp[i] = max(0, dp[i-1]) + nums[i]
        max_sum = max(max_sum, dp[i])

    return max_sum

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
n = [-2,1,-3,4,-1,2,1,-5,4]

print(maxSubarray(n))