class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # same as best sum problem

        memo = {}
        def dfs(cur):
            if cur in memo:
                return memo[cur]
            if cur == 0:
                memo[cur] = 0
                return 0
            res = 1e9
            for c in coins:
                if cur - c >= 0:
                    res = min(res, 1 + dfs(cur-c))
            memo[cur] = res
            return res


        res = dfs(amount)
        return res if res < 1e9 else -1
