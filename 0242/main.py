# 242. Valid Anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_dict = {}
        
        for c in s:
            if c in count_dict:
                count_dict[c] += 1
            else:
                count_dict[c] = 1
        
        for c in t:
            if c in count_dict:
                count_dict[c] -=1
            else: # char in t doesn't exist in s
                return False
        
        for k in count_dict.keys():
            if count_dict[k] != 0:
                return False
        
        return True