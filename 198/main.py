# 198. House Robber
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        
        # rob(i) = max(nums[i] + rob(i+2), rob(i+1)) # use memoization for already calculated values
        # rob = max(arr[0] + rob[2:n], rob[1:n])
        # [rob1, rob2, n, n+1, ...]
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
