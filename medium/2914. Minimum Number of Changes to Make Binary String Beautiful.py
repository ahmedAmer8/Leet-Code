class Solution:
    def minChanges(self, s: str) -> int:
        # count the # of changes in any two consecutive chars
        res = 0
        for i in range(0, len(s)-1, 2):
            if s[i] != s[i+1]:
                res += 1
        return res
