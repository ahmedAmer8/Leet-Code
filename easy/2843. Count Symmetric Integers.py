class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def isSymmetric(num):
            l = len(str(num))
            if l & 1:
                return False
            s1 = s2 = 0
            l /= 2
            while num:
                d = num % 10
                num //= 10
                if l > 0:
                    s1 += d
                    l -= 1
                else:
                    s2 += d
            return s1 == s2
        
        res = 0
        for n in range(low, high+1):
            res += isSymmetric(n)
        
        return res
