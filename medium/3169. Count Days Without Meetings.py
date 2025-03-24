class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key= lambda x:(x[0], x[1]))
        count, cur = 0, 0
        for s, e in meetings:
            count += max(0, s - cur - 1)
            cur = max(cur, e)
        
        return count + days - cur
