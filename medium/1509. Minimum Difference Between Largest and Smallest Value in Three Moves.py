class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        
        max_four = sorted(heapq.nlargest(4, nums))
        min_four = sorted(heapq.nsmallest(4, nums))

        res = float('inf')
        for i in range(4):
            res = min(res, max_four[i] - min_four[i])
        
        return res
