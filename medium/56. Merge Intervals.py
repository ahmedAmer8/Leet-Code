class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        i = 0
        for s, e in intervals[1:]:
            if s <= res[i][1]:
                res[i][0] = min(s, res[i][0])
                res[i][1] = max(e, res[i][1])
            else:
                res.append([s, e])
                i += 1

        return res
