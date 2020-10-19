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