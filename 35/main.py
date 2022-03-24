# 35. Search Insert Position
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        
        while(low<=high):
            mid = int((low + high)/2)
            
            if(nums[mid] < target): # go to right
                low = mid + 1
            elif (nums[mid] > target): # go to left
                high = mid - 1
            else:
                return mid
            
        return low
