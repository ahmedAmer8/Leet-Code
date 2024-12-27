class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        res = prev = float('-inf')

        for i, v in enumerate(values):
            res = max(res, prev+(v-i))
            prev = max(prev, v+i)
        return res
