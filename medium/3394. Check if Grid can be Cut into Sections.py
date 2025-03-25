class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def solve(intervals):
            intervals.sort()
            count = 0
            max_end = intervals[0][1]
            for s, e in intervals:
                if max_end <= s:
                    count += 1
                max_end = max(max_end, e)
            return count >= 2

        x = [[rec[0], rec[2]] for rec in rectangles]
        y = [[rec[1], rec[3]] for rec in rectangles]
        return solve(x) or solve(y)
