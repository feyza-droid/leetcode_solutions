# 796. Rotate String
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal:
            return True

        n = len(s)-1
        for i in range(n):
            if s[0:i] == goal[n-i:n] and s[i+1:n] == goal[0:n-i-1]:
                return True

        return False