class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        
        l, r = 0, len(height) - 1
        area_max = (r - l) * min(height[l], height[r])
        
        while l < r:
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
            area_max = max(area_max, (r - l) * min(height[l], height[r]))
        
        return area_max

def main():
    # 11 https://leetcode.com/problems/container-with-most-water/

if __name__ == "__main__":
    main()