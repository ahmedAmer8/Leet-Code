class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        times = []
        for b,d in logs:
            times.append((b, -1))
            times.append((d-1, 1))
        res = [0, 0]
        count = 0
        for year, val in sorted(times):
            count -= val
            if count > res[0]:
                res[0] = count
                res[1] = year
        return res[1]
