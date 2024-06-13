class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        Max = float(-inf)
        prev = 0
        for i in range(len(gain)):
            val = prev + gain[i]
            Max = max(val, Max)
            prev = val
        return max(Max, 0)
