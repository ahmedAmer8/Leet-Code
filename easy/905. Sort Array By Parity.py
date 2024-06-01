class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        a1 = [i for i in nums if i % 2 == 0]
        a2 = [i for i in nums if i % 2 == 1]
        return a1 + a2
