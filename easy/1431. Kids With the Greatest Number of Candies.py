class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx = max(candies)
        return [True if c + extraCandies >= mx else False for c in candies ]
