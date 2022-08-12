# 125. Valid Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = ''.join(filter(str.isalnum, s)).lower()
        
        l = 0
        r = len(s) - 1
        
        is_palindrome = True
        
        while(True):
            if l > r:
                break
                
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                is_palindrome = False
                break
                
        return is_palindrome
