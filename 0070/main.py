#70. Climbing Stairs
#memoization solution
class Solution:
    def climbStairs(self, n: int) -> int:
        mem = (n+1) * [0]
        mem[0] = 1
        mem[1] = 1
        return self.distinct_ways(n, mem)
        
    def distinct_ways(self, n, mem):
        if n < 2:
            return mem[n]
        
        if mem[n-2] == 0:
            mem[n-2] = self.distinct_ways(n-2, mem)
            
        if mem[n-1] == 0:
            mem[n-1] = self.distinct_ways(n-1, mem)       
        
        mem[n] = mem[n-1] + mem[n-2]
        return mem[n]
