class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        return sum(i == 0 for i in accumulate(nums))
