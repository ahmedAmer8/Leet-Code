class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opened = res = 0
        for ch in s:
            if ch == '(':
                opened += 1
            else:
                opened -= 1
            
            if opened < 0:
                res += 1
                opened = 0
        return res + opened
