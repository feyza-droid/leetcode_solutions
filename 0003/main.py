# 3. Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)

        if l == 0:
            return 0
        
        if l == 1:
            return 1
        
        largest_count = 0
        start = 0
        end = 1
        count = 0
        
        while (end != l):
            found_index = s.find(s[end], start, end) # can be replaced with dictionary which holds characters with their indexes
            if  found_index == -1:
                count = end - start + 1
                end += 1
            else:
                if count > largest_count:
                    largest_count = count
                count = 0
                start = found_index + 1

        if count > largest_count:
            largest_count = count
                
        return largest_count
