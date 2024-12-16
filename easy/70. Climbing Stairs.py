class Solution:
    def climbStairs(self, n: int) -> int:
        DP = {0:1, 1:1}
        def rec(n):
            if n in DP:
                return DP[n]
            if n == 1:
                return 1
            if n == 2:
                return 2
            DP[n] = rec(n-1) + rec(n-2)
            return DP[n]
        return rec(n)
    
