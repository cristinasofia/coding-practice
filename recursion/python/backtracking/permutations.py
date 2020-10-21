# 46 

def permute(nums):
    def backtrack(nums, path):
        if len(nums) == 0:
            output.append(path[:])
        else:
            for i in nums:
                #path.append(i)
                next_nums = nums[:]
                next_nums.remove(i)

                backtrack(next_nums, path + [i])
                #path.pop()
                
        
    output = []
    backtrack(nums, [])
    return output

# 47

def permuteUnique(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    
    def backtrack(nums, path):
        if len(nums) == 0:
            output.append(path)
        else:
            for i in list(set(nums)):
                next_nums = nums[:]
                next_nums.remove(i)
                backtrack(next_nums, path + [i])
    
    output = []
    backtrack(nums, [])
    return output