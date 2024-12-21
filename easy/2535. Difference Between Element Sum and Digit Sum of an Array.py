class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        def digitsSum(n):
            res = 0
            while n:
                res += n % 10
                n //= 10
            return res
        arrSum = sum(nums)
        allDigitsSum = 0
        for n in nums:
            allDigitsSum += digitsSum(n)
        return abs(allDigitsSum - arrSum)
