class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        length = 2**n - 1
        def solve(length, k):
            if length == 1:
                return '0'
            m = length // 2
            if k <= m:
                return solve(m, k)
            elif k > m+1:
                b =  solve(m, 1 + length - k)
                return '0' if b == '1' else '1'
            else:
                return '1'

            
        return solve(length, k)
