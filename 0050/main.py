# 50. Pow(x, n)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = n * -1
        
        saved_pow = {
            0: 1,
            1: x,
            2: x*x
        }
        
        return self.recursivePow(n, saved_pow)  
    
    def recursivePow(self, n, saved_pow):
        if n in saved_pow: # base case
            return saved_pow.get(n)
        else:
            right = int(n / 2)
            left = n - right
            
            if not left in saved_pow:
                saved_pow[left] = self.recursivePow(left, saved_pow)
                
            if not right in saved_pow:
                saved_pow[right] = self.recursivePow(right, saved_pow)
                
            saved_pow[n] = saved_pow[left] * saved_pow[right]
            
            return saved_pow[n]
