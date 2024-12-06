class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1
        for i in range(n):
            pos = abs(nums[i])
            if pos > n:
                continue
            if nums[pos -1] > 0:
                nums[pos - 1] *= -1
        for i in range(1, n+1):
            if nums[i-1] >= 0:
                return i
        return n + 1
