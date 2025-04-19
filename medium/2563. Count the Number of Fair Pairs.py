class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        def last_valid(l, target):
            r = n -1
            while l <= r:
                m = l + (r - l) // 2
                if nums[m] <= target:
                    l = m + 1
                else:
                    r = m - 1
            return r
        
        def first_valid(l, target):
            r = n -1
            while l <= r:
                m = l + (r - l) // 2
                if nums[m] >= target:
                    r = m - 1
                else:
                    l = m + 1
            return l
        
        res = 0
        for i in range(n-1):
            l = first_valid(i+1, lower-nums[i])
            r = last_valid(i+1, upper-nums[i])
            res +=  r - l + 1
        
        return res
        

                
