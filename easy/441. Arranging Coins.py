class Solution:
    def arrangeCoins(self, n: int) -> int:
        ans = 0
        l, r = 1, n
        while l <= r:
            m = l + (r-l)//2
            temp = m*(m+1)/2
            if temp <= n:
                ans = m
                l = m+1
            else:
                r = m-1
        return ans
                
