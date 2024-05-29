class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_position = 0
        size = len(nums)
        for i in range(size):
            # break if we cannot reach this position 
            # or if we are already can reach the last index
            if max_position < i or max_position >= size -1 : break
            i_max_position = i + nums[i]
            max_position = max(max_position, i_max_position)
        return max_position >= size -1
