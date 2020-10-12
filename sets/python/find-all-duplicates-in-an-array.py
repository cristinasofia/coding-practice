# 442 https://leetcode.com/problems/find-all-duplicates-in-an-array/

# appraoch 1
def findDuplicates1(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    i = 1
    s = set(nums) # O(n)
    res = []

    for i in nums: # O(n)
        if i in s: # O(1)
            s.discard(i)  # O(1)
        else:
            res.append(i)
        i += 1

    return res

# approach 2
def findDuplicates2(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    res = []
    
    for i in nums:
        if nums[abs(i)-1] >= 0:
            nums[abs(i)-1] *= -1    
            # element is marked as negative in the array 
            # so when i is a duplicate
            # it will not meet the condition of the if statement
            # and instead (else) be appended to res
        else:
            res.append(abs(i))

    return res