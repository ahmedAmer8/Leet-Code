class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        start = meetings[0][0]
        end = meetings[0][1]
        for s, e in meetings[1:]:
            if s <= end:
                end = max(end, e)
            else:
                days -= (end - start + 1)
                start = s
                end = e
        return days - (end - start + 1)
