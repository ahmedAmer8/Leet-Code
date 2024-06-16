class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums, reverse=True)
        n = len(nums)
        freq = Counter(nums)
        res = [0]*n
        for i in range(n):
            res[i] = n - sorted_nums.index(nums[i]) - freq[nums[i]]
        return res
