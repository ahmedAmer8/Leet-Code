class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        n = len(encoded)
        res = [0] * (n+1)
        res[0] = first
        for i in range(n):
            res[i+1] = encoded[i] ^ res[i]
        return res
