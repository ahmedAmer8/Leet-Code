class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left, right = 0, sum(nums)
        n = len(nums)
        res = [0]*n
        for i in range(n):
            right -= nums[i]
            res[i] = abs(right - left)
            left += nums[i]

        return res
