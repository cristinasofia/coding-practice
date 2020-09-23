def nextPermutation(self, nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    
    n = len(nums)
    i = n - 1
    while i > 0 and nums[i-1] >= nums[i]: # find largest number index in nums
        i -= 1
    
    if i > 0:
        l, r = i, n-1
        while l <= r:
            m = l + (r-l) //2
            if nums[i-1] < nums[m]:
                l = m + 1
            else:
                r = m -1
        nums[i-1], nums[l-1] = nums[l-1], nums[i-1]

    l, r = i, n-1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1
            