# https://leetcode.com/problems/search-in-rotated-sorted-array/solution/

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l+r)//2
            
            if nums[m] == target:
                return m
            elif nums[l] <= nums[m]: 
                # if left is smaller than mid, then left is sorted
                # e.g. 4 < 7
                if nums[l] <= target < nums[m]:
                    # if target is within l and m indicies, then go left
                    # e.g. target == 6
                    r = m - 1
                else:
                    # e.g. target == 2
                    l = m + 1
            else:
                # if right is bigger than mid, then right is sorted
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        
        return -1

def main():


if __name__ == "__main__":
    main()