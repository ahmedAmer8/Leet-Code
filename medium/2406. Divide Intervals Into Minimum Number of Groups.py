class Solution:
    def minGroups(self, intervals):
        A = []
        for a, b in intervals:
            A.append((a, 1))
            A.append((b+1, -1)) # shift all end times by 1 to avoid start = end
        cur = res = 0
        for t in sorted(A):
            cur += t[1]
            res = max(res, cur)
        return res
