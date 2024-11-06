class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            pivot = nums[i]
            idx = i
            for j in range(i+1, n):
                if nums[j] < nums[i]:
                    if bin(nums[j]).count("1") == bin(nums[i]).count("1"):
                        pivot = nums[j]
                        idx = j
                    else:
                        return False
            nums[idx], nums[i] = nums[i], nums[idx]
        return True
