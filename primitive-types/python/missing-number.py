# 268 https://leetcode.com/problems/missing-number/

# using sets
def missingNumber_1(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    n = len(nums)
    s = set(x for x in range(0,n+1))
    
    for i in nums:
        s.discard(i)
    
    return s.pop()

# using gauss
def missingNumber_2(nums):
    n = len(nums)
    gauss = (n) * (n+1) // 2
    total = sum(nums)

    return gauss - total

# using bits
def missingNumber_3(nums):
    return 0