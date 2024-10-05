class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        counts = Counter(s1)
        def sameCounter(c):
            for k, v in c.items():
                if counts[k] != v:
                    return False
            return True
        
        l = 0
        for i in range(len(s1)-1, len(s2)):
            if sameCounter(Counter(s2[l:i+1])):
                return True
            l += 1
        return False
