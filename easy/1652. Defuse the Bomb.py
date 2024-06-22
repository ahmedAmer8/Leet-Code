class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        l, r = 1, k
        size = len(code)
        res = [0]*size
        if k == 0: return res
        elif k < 0:
            r *= -1
            code.reverse()
        i = 0
        s = sum(code[l:r + 1])
        while i < size:
            res[i] = s
            s -= code[l]
            l = (l+1) % size
            r = (r+1) % size
            s += code[r]
            i += 1
        return res if k > 0 else list(reversed(res))
