# 278. First Bad Version
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:        
        low = 1
        high = n
        is_last_bad = False
        
        while(low <= high):            
            mid = int((low + high) / 2)
            if(isBadVersion(mid)): # look at left
                high = mid - 1
                is_last_bad = True
            else: # look at right
                low = mid + 1
                is_last_bad = False
                
        if is_last_bad:
            return mid
        else:
            return mid+1
