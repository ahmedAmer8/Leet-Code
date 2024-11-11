def is_prime(n):
    for i in range(2, int(sqrt(n))+1): 
        if n % i == 0: 
            return False
    return True

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        # at each time subtract the largest prime number you can
        max_num = max(nums)
        primes = []
        for i in range(max_num-1, 1, -1):
            if is_prime(i):
                primes.append(i)
        prev = 0
        for i in range(len(nums)):
            for p in primes:
                if nums[i] - p > prev:
                    nums[i] -= p
                    break
            if nums[i] <= prev:
                return False
            prev = nums[i]
        print(nums)
        return True
        
