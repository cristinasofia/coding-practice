# 136 https://leetcode.com/problems/single-number/

# using sets
def singleNumber_1(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    s = set()
    
    for i in nums:
        if i in s:
            s.remove(i)
        else:
            s.add(i)
    
    return s.pop()

# using gauss
 def singleNumber_2(nums):   
    return 2 * sum(set(nums)) - sum(nums)

# using bits
def singleNumber_3(nums):
    return 0