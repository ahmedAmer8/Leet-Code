class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        special_subarrays = []

        def binary_search(value):
            l, r = 0, len(special_subarrays)
            while l <= r:
                m = l + (r-l)//2
                start, end = special_subarrays[m][0], special_subarrays[m][1]
                if start <= value <= end:
                    return start, end
                elif value > end:
                    l = m + 1
                else:
                    r = m -1
        start = 0
        for i in range(n-1):
            if nums[i] & 1 == nums[i+1] & 1:
                special_subarrays.append((start, i))
                start = i+1
        special_subarrays.append((start, n-1))
        res = []
        for s, e in queries:
            start, end = binary_search(s)
            res.append(start <= e <= end)
        return res
            
        
