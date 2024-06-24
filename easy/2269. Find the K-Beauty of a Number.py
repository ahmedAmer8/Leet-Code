class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        l, r = 0, k
        num = str(num)
        res = 0
        while r <= len(num):
            n = int(num[l:r])
            if n != 0 and int(num) % n == 0:
                res += 1
            l, r = l+1, r+1
        return res
