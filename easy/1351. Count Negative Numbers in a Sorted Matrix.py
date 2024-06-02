class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0
        for i in grid:
            # find the # -ve in each row
            n = len(i)
            ans = n
            l, r = 0, n-1
            while l<=r:
                m = l + (r-l)//2
                if i[m] >= 0:
                    l = m + 1
                else:
                    ans = m
                    r = m - 1
            res += n-ans
        return res
