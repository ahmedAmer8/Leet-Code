class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum, right_sum = 0, sum(nums)
        for i, item in enumerate(nums):
            right_sum -= item
            if left_sum == right_sum:
                return i
            left_sum += item
        return -1
