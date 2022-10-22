# 647. Palindromic Substrings
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            # odd length substrings
            l, r = i, i
            
            odd = self.calculate(s, l, r)
            
            # even length substrings
            l, r = i, i+1
            
            even = self.calculate(s, l, r)
        
            count += odd
            count += even
        
        return count
    
    def calculate(self, s, l, r):
        count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            count += 1
            
        return count
