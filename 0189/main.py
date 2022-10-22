# 189. Rotate Array
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        new_nums = [0] * l

        for i in range(l):
            j = (i + k) % l
            new_nums[j] = nums[i]
            
        for i in range(l):
            nums[i] = new_nums[i]
            
