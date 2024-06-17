class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        k = int(len(piles)/3)

        return sum([piles[i] for i in range(len(piles)-2, k-1, -2)])
