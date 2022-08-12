# 13. Roman to Integer
class Solution:
    def romanToInt(self, s: str) -> int:        
        symbols = {}
        symbols['I'] = 1
        symbols['V'] = 5
        symbols['X'] = 10
        symbols['L'] = 50
        symbols['C'] = 100
        symbols['D'] = 500
        symbols['M'] = 1000
        
        i = 0
        l = len(s)
        total = 0
        
        while(i+1 < l):
            if symbols[s[i]] >= symbols[s[i+1]]:
                total += symbols[s[i]]
            else:
                total -= symbols[s[i]]
            i += 1
        
        total += symbols[s[i]]
        return total
