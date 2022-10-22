# 11. Container With Most Water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        
        max_water = 0
        while l != r:
            w = r-l
            if height[l] > height[r]:
                h = height[r]
                r -= 1
            else:
                h = height[l]
                l += 1
                
            water = w * h
            if water > max_water:
                max_water = water
                
        return max_water
