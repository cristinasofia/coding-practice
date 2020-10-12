# 11 https://leetcode.com/problems/container-with-most-water/
def maxArea(height):
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
