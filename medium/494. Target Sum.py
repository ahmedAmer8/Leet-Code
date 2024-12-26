class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        N = len(nums)
        dp = {}
        def solve(i, curSum):
            if i == N:
                return 1 if curSum == target else 0
            if (i, curSum) in dp:
                return dp[(i, curSum)]
            dp[(i, curSum)] = (solve(i+1, curSum + nums[i]) + 
                    solve(i+1, curSum - nums[i]))
            return dp[(i, curSum)]
        return solve(0, 0)
