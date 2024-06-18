class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        hashmap = {}
        n = len(s)
        for i in range(n):
            hashmap[s[i]] = i
        res = 0
        for i in range(n):
            res += abs(hashmap[t[i]] -  i)
        return res
