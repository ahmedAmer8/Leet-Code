from math import ceil
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        freq = [ceil((n-i)*(i+1)/2) for i in range(n)]
        return sum(i*j for i, j in zip(freq, arr))
        

