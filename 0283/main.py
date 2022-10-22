# 283. Move Zeroes
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        i = 0
        for j in range(1,l):
            if nums[i] == 0:
                if nums[j] != 0: # swap
                    temp = nums[j]
                    nums[j] = nums[i]
                    nums[i] = temp
                    i += 1
            else:
                i += 1
