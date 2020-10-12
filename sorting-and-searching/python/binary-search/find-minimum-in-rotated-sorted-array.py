# 153 https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    l, r = 0, len(nums) - 1
    
    while l < r:
        m = (l + r) //2
        if nums[m] < nums[r]:
            r = m # min is between l and m (go left)
        else:
            l = m + 1 # min is between m + 1 and r (go right)
        
    return nums[l] # changing l to r finds maximum element

# 154 https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

def findMin2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    l, r = 0, len(nums) - 1
    
    while l < r:
        m = (l + r)//2

        if nums[l] == nums[m] == nums[r]:
            l += 1
            r -= 1
        elif nums[m] <= nums[r]:
            r = m
        else:
            l = m + 1

    return nums[l]

# CASE 1: [1, 3, 3]
# CASE 2: [3, 1, 1]
# CASE 3: [10, 1, 10, 10, 10]