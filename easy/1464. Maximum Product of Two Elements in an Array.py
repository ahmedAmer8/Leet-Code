class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 2:
            return (nums[0]-1) * (nums[1]-1)

        first = second = float(-inf)
        for i in range(n):
            if nums[i] > first:
                second = first
                first = nums[i]
            elif nums[i] > second:
                second = nums[i]
        return (first-1) * (second-1)
