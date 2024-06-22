class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd = [i for i in range(len(nums)) if nums[i] % 2 == 1]
        res = 0
        l, r = -1, k
        s, e = 0, k-1
        while e < len(odd):
            if l >= 0:
                nBefore = odd[s] - odd[l] - 1
            else:
                nBefore = odd[s]
            if r < len(odd):
                nAfter = odd[r] - odd[e] - 1
            else:
                nAfter = len(nums) - odd[e] - 1
            res += (nAfter+1)*(nBefore+1)
            s, e, l, r = s+1, e+1, l+1, r+1
        return res            
