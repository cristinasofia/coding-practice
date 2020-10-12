# 448 https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/submissions/

# approach 1
def findDisappearedNumbers1(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    
    res = []
    s = set(nums) # O(n)
    
    i = 1
    while i < len(nums) + 1: # O(n)
        if i not in s: # O(1)
            res.append(i)
        i += 1
    
    return res

# approach 2
def findDisappearedNumbers2(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    res = []

    for i in nums:
        if nums[abs(i)-1] >= 0:
            nums[abs(i)-1] *= -1

    for i, n in enumerate(nums):
        if n >= 0:
            res.append(i+1)
    
    return res