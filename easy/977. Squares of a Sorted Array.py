class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        l, r = 0, len(nums)-1
        cur = r
        while l <= r:
            if nums[l]**2 < nums[r]**2:
                res[cur] = nums[r]**2
                r -= 1
            else:
                res[cur] = nums[l]**2
                l += 1
            cur -= 1

        return res
