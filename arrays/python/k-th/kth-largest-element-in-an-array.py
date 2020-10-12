
def by_sorting(nums, k):
    return sorted(nums, reverse=True)[k-1]

def by_minheap(nums, k):
    import heapq
    return heapq.nlargest(k, nums)[-1]

def by_quickselect(nums, k):

    # pivot index partition
    def partition(l, r):
        # this is the pivot index
        low = l
        while l < r:
            # put smaller elements on left,
            # put larger elements on right
            if nums[l] < nums[r]:
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1

        # replace pivot element
        nums[low], nums[r] = nums[r], nums[low]
        return low

    def findKthSmallest(l, r, k):
        if nums:
            # make a guess
            pos = partition(l, r)
            # check your guess
            if k > pos:
                # go right
                return findKthSmallest(pos+1, r, k)
            elif k < pos:
                # go left
                return findKthSmallest(l, pos-1, k)
            else:
                return nums[pos]

    # kth largest element also means (len(nums) - k)th smallest
    return findKthSmallest(0, len(nums) - 1, len(nums) - k)


nums = [3, 2, 1, 5, 6, 4]
k = 2
nums2 = [5, 5, 4, 3, 2, 3, 1, 2, 6]
k2 = 4

# O(nlogn)
by_sorting(nums, k)

# O(k+(n-k)logk)
by_minheap(nums, k)

# O(n)
print(by_quickselect(nums2, k2))