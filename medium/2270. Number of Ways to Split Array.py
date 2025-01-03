class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0]*n
        prefix[0] = nums[0]
        suffix = [0]*n
        suffix[n-1] = nums[n-1]
        for i in range(1, n):
            prefix[i] += prefix[i-1] + nums[i]
            suffix[n-i-1] = suffix[n-i] + nums[n-i-1]
        
        print(prefix, suffix)
        res = 0
        for i in range(n-1):
            res += 1 if prefix[i] >= suffix[i+1] else 0
        return res
