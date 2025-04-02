class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = left_max = max_diff = 0
        for n in nums:
            res = max(res, n * max_diff)
            max_diff = max(max_diff, left_max - n)
            left_max = max(left_max, n)
        
        return res
