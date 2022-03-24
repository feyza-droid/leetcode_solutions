# 557. Reverse Words in a String III
class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        
        l = len(s)
        start_index_list = list()
        end_index_list = list()
        
        start_index_list.append(0)
        
        for i in range(l):
            if s[i] == ' ':
                start_index_list.append(i+1)
                end_index_list.append(i-1)        
        end_index_list.append(l-1)
        
        indx_len = len(end_index_list)
        for indx in range(indx_len):
            start = start_index_list[indx]
            end = end_index_list[indx]
            self.reverseOneWord(s, start, end)
        
        return "".join(s)
        
    def reverseOneWord(self, s, start, end):
        i = start
        j = end
        l = (end - start) + 1
        mid = start + int(l / 2)
        
        while(True):
            if i == mid:
                break
            else: # swap
                temp = s[i]
                s[i] = s[j]
                s[j] = temp
                
                i += 1
                j -= 1
