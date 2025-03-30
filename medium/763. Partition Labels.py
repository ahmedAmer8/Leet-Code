class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurance = {}
        for i,ch in enumerate(s):
            last_occurance[ch] = i
        
        res = []
        cur = length = 0
        for l in range(len(s)):
            length = max(length, last_occurance[s[l]])
            if length == l:
                res.append(length - cur + 1)
                cur += res[-1]
        
        return res
