# 34 Find First and Last Position of Element in Sorted Array
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        start = 0 
        end = l - 1
        mid = 0
        
        found_indexes = [-1, -1]
        
        while(start <= end):
            mid = int((start + end) / 2)
            if nums[mid] == target:
                # found, search for prev and next
                found_indexes = self.searchForSame(mid, l, nums, target, found_indexes)
                break                            
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        
        
        return found_indexes
    
    def searchForSame(self, mid, l, nums, target, found_indexes):
        found_indexes[0] = mid
        found_indexes[1] = mid
        prev = mid - 1
        later = mid + 1
        
        while(prev != -1):
            if nums[prev] == target:
                found_indexes[0] = prev
                prev -= 1
            else:
                break

        while(later != l):
            if nums[later] == target:
                found_indexes[1] = later
                later += 1
            else:
                break
                
        return found_indexes
