class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first_occurance = last_occurance = -1
        found = False
        n = len(nums)
        l, r = 0, n-1
        while l <= r:
            m = l + (r-l)//2
            if nums[m] == target: found= True
            if nums[m] >= target:
                first_occurance = m
                r = m -1
            else:
                l = m + 1

        l, r = 0, n-1
        while l <= r:
            m = l + (r-l)//2
            if nums[m] == target: found= True
            if nums[m] <=  target:
                last_occurance = m
                l = m + 1
            else:
                r = m -1
        return [first_occurance, last_occurance] if found else [-1, -1]
