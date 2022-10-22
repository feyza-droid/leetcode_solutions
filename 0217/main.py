# 217. Contains Duplicate
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count_dict = {}
        
        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1
        
        for num in nums:
            if count_dict[num] >= 2:
                return True
                
        return False
