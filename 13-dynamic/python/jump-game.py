
def canJump1(nums):
    last = len(nums) - 1

    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] >= last:
            last = i
    
    return last == 0

def canJump2(nums):
    jumps = 0
    end, farthest = 0, 0

    for i in range(len(nums)):
        farthest = max(farthest, i + nums[i])
        if i == end:
            jumps += 1
            end = farthest
    
    return jumps


# Jump Game 1
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Determine if you are able to reach the last index.

n1 = [2, 3, 1, 1, 4]
# True

n2 = [3, 2, 1, 0, 4]
# False

print(canJump1(n1))
print(canJump1(n2))

# Jump Game 2
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Your goal is to reach the last index in the minimum number of jumps.

n1 = [2, 3, 1, 1, 4]
# 2

print(canJump2(n1))
print(canJump2(n2))

