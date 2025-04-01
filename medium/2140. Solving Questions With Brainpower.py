class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = {}
        def solve(i):
            if i >= len(questions):
                return 0
            if i in dp:
                return dp[i]
            dp[i] = max(questions[i][0] + solve(i+questions[i][1]+1), solve(i+1))
            return dp[i]
        return solve(0)
