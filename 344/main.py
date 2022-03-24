# 344. Reverse String
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)
        i = 0
        j = l - 1
            
        mid = int(l / 2)
        while(True):
            if i == mid:
                break
            else: # swap
                temp = s[i]
                s[i] = s[j]
                s[j] = temp
                
                i += 1
                j -= 1
            
