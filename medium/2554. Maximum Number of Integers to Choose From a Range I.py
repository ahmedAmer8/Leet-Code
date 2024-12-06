class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        count, curSum, i = 0, 0, 1
        while i <= n:
            if i not in banned and i + curSum <= maxSum:
                curSum += i
                count += 1
            i += 1
        return count
