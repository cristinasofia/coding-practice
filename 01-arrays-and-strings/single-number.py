
import collections
def singleNumber1(nums):
    return 0

def singleNumber2_method1(self, nums):
    """
    input = [2,2,3,2]
    (3 * (2 + 3) - (2+2+2+3)) = 6
    6/2 = 3

    """

    return (3 * sum(set(nums)) - sum(nums)) // 2

def singleNumber2_method2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    d = collections.Counter(nums)
    for k in d.keys():
        if d[k] == 1:
            return k