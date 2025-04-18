class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts = Counter(arr)
        res = len(counts)
        for n in sorted(counts.values()):
            if k - n >= 0:
                k -= n
                res -= 1
            else:
                return res
        return res

