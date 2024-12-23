class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {n:0, n+1:0}
        def rec(i):
            if i in dp:
                return dp[i]
            first = nums[i] + rec(i+2)
            second = rec(i+1)
            dp[i] = max(first, second)
            return dp[i]
        return rec(0)
