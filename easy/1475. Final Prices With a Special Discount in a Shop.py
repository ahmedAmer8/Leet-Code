class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = prices.copy()
        stack = []
        for i,p in enumerate(prices):
            while stack and p <= stack[-1][1]:
                idx, v = stack.pop()
                res[idx] -= p
            stack.append((i, p))
        return res
