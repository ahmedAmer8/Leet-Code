class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        # number of subarrays in valid array with length n = N*(N+1)/2
        left = right = 0
        res = 0
        win_max = nums[0]
        win_min = nums[0]
        while right < len(nums):
            win_min= min(win_min, nums[right])
            win_max = max(win_max, nums[right])
            
            if win_max - win_min > 2:
                n = right - left
                res += n*(n+1)/2
                left = right
                win_max = win_min = nums[right]
                while abs(nums[right] - nums[left-1]) <= 2:
                    left -= 1
                    win_max = max(win_max, nums[left])
                    win_min= min(win_min, nums[left])
                if left < right:
                    n = right - left
                    res -= n*(n+1)/2
            right += 1
        n = right - left
        res += n*(n+1)/2
        return int(res)
