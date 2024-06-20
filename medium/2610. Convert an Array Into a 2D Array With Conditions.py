class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        c = defaultdict(int)
        res = []
        for n in nums:
            row = c[n]
            if row == len(res):
                res.append([])
            res[row].append(n)
            c[n] += 1

        return res
