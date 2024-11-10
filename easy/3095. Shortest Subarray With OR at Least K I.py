class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        shortest = 51
        for i in range(len(nums)):
            cur = 0
            for j in range(i, len(nums)):
                cur |= nums[j]
                if cur >= k:
                    shortest = min(shortest, j-i+1)
                    break
        return shortest if shortest < 51 else -1
