class Solution:
    def removeStars(self, s: str) -> str:
        skip = 0
        res = ""
        for i in range(len(s)-1, -1, -1):
            if s[i] == '*':
                skip += 1
            if skip == 0 and s[i] != '*':
                res += s[i]
            if s[i] != '*' and skip > 0:
                skip -= 1
        return res[::-1]
