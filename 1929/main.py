# 1929. Concatenation of Array
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            ans.append(n)

        for n in nums:
            ans.append(n)

        return ans