# 5. Longest Palindromic Substring
class Solution:
    def longestPalindrome(self, s: str) -> str:
        sub = ""
        sub_len = 0
        
        for i in range(len(s)):
            # odd case
            l, r = i, i
            sub, sub_len = self.comparison(s, sub, sub_len, l, r)
            
            # even case
            l, r = i, i+1
            sub, sub_len = self.comparison(s, sub, sub_len, l, r)
            
        return sub
            
    def comparison(self, s, sub, sub_len, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > sub_len:
                sub_len = r - l + 1
                sub = s[l:r+1]
            l -= 1
            r += 1
        
        return sub, sub_len
