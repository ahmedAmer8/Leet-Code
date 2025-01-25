
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # we can omit the 2d list and use three variables
        # cuz we only need cur, next1, next2
        # dp = [[0 for _ in range(2)] for _ in range(n+2)]

        cur = [0]*2    # for buy = 1 and buy = 0
        next1 = [0]*2
        next2 = [0]*2
        
        for i in range(n-1, -1, -1):
            # we can omit the innver loop and make the dp runs for 0 and 1
            # if buy = 1
            cur[1] = max(-prices[i] + next1[0], next1[1])
            # if buy = 0
            cur[0] = max(prices[i] + next2[1], next1[0])
            next2 = next1.copy()
            next1 = cur.copy()

        return cur[1]
