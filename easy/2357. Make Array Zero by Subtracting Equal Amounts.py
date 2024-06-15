class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        subtracted = 0
        nums = sorted(set(nums))
        mx = nums[-1]
        count = 0
        for i in nums:
            if i != 0:
                count += 1
                subtracted += i - subtracted
                if mx - subtracted <= 0: return count
        return 0
