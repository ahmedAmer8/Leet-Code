class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(start, end):
            prev = nums[start]
            prev2 = 0
            for i in range(start+1, end):
                cur = max(nums[i] + prev2, prev)
                prev2 = prev
                prev = cur
            return prev
        if len(nums) == 1:
            return nums[0]
        return max(helper(0, len(nums)-1), helper(1, len(nums)))
