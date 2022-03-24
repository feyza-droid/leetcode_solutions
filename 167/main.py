# 167. Two Sum II - Input Array Is Sorted
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l = len(numbers)
        i = 0
        j = l-1
        indexes = [None] * 2
        
        while (i < l and (j >= 0)):
            temp_sum = numbers[i] + numbers[j]
            if temp_sum == target:
                indexes[0] = i+1
                indexes[1] = j+1
                break
            elif temp_sum > target:
                j -= 1
            else:
                i += 1
                
        return indexes
