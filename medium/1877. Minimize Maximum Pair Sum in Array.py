class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        L, R = 0, len(nums) - 1
        res = float('-inf')
        while L < R:
            res = max(nums[R]+ nums[L], res)
            L += 1
            R -= 1
        return res
