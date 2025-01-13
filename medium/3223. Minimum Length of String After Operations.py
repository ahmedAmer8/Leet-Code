class Solution:
    def minimumLength(self, s: str) -> int:
        c = Counter(s)
        res = len(s)
        for freq in c.values():
            while freq >= 3:
                res -= 2
                freq -= 2
        return res
