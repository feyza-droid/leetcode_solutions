# 443. String Compression
class Solution:
    def update(self, chars: List[str], start, count, i):
        count_list = list(str(count))
        index = start+len(count_list)

        chars[start:index] = count_list # write count's digits to chars list
        del chars[index:i] # remove compressed chars
        i = index # continue right after removed chars
        
        return i
    
    def compress(self, chars: List[str]) -> int:
        start, count, i = 1, 1, 1
        
        while True:
            if i == len(chars):
                break
            
            if chars[i] == chars[i-1]: # same, increment count of the same char
                count += 1
            else: # not same, change happens
                if count != 1:
                    i = self.update(chars, start, count, i)
                
                start = i + 1
                count = 1

            i += 1
    
        if count != 1: # to compress latest char if number of occurrence is more than 1
            i = self.update(chars, start, count, i)
            
        return len(chars)