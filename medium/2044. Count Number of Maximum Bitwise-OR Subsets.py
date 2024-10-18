class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # if you take or of a number with another one it will increase or stay the
        # same so we can take or of all the nums and this will give the max or
        max_or = 0
        for n in nums:
            max_or |= n
        res = [0]
        def dfs(i, cur):
            if i == len(nums):
                res[0] += 1 if cur == max_or else 0
                return
            temp = cur | nums[i] # do something
            dfs(i+1, temp)       # go recursive
            dfs(i+1, cur)        # undo
        dfs(0, 0)
        return res[0]

        
