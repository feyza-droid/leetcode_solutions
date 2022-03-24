# 977. Squares of a Sorted Array
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # first find the smallest square element (the one closest to 0)
        low = 0
        high = len(nums) - 1
        target = 0
        
        while(low <= high):
            mid = int((low + high) / 2)
            if nums[mid] > target: # go to left
                high = mid - 1
            elif nums[mid] < target: # go to right
                low = mid + 1
            else: # found
                break
        
        if not (len(nums) == 1 or len(nums) == 2):
            if (mid - 1 >= 0) and (abs(nums[mid-1])) < (abs(nums[mid])):
                found = mid - 1
            elif (mid + 1 <= (len(nums)-1)) and (abs(nums[mid+1])) < (abs(nums[mid])):
                found = mid + 1
            else:
                found = mid
        else:
            found = mid
        
        # then go to left and right of the root of smallest square element (with two pointers)
        plus_pointer = found + 1
        minus_pointer = found - 1
        
        square_list = [None] * len(nums)
        square_list[0] = nums[found] * nums[found]
        
        i=1
        while(minus_pointer >= 0 and (plus_pointer <= len(nums) - 1)):
            if abs(nums[minus_pointer]) < nums[plus_pointer]:
                square_list[i] = nums[minus_pointer] * nums[minus_pointer]
                minus_pointer -= 1
                i += 1
            elif abs(nums[minus_pointer]) > nums[plus_pointer]:
                square_list[i] = nums[plus_pointer] * nums[plus_pointer]
                plus_pointer += 1
                i += 1
            else:
                square_list[i] = nums[minus_pointer] * nums[minus_pointer]
                square_list[i+1] = nums[plus_pointer] * nums[plus_pointer]
                plus_pointer += 1
                minus_pointer -= 1
                i += 2
                
        while minus_pointer >= 0:
            square_list[i] = nums[minus_pointer] * nums[minus_pointer]
            minus_pointer -= 1
            i += 1
            
        while (plus_pointer <= len(nums) - 1):
            square_list[i] = nums[plus_pointer] * nums[plus_pointer]
            plus_pointer += 1
            i += 1
        
        return square_list
