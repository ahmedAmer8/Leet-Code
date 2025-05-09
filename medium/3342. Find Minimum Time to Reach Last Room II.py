class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])

        arrival_time = [[float('inf')] * m for _ in range(n)]
        arrival_time[0][0] = 0

        min_heap = [(0, 0, 0, 1)]

        while min_heap:
            time, x, y, cost = heapq.heappop(min_heap)

            if (x, y) == (n-1, m-1):
                return time

            if time > arrival_time[x][y]:
                continue

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = x+dr, y+dc
                if 0 <= nr < n and 0 <= nc < m:
                    new_time = max(time, moveTime[nr][nc]) + cost
                    if new_time < arrival_time[nr][nc]:
                        arrival_time[nr][nc] = new_time
                        new_cost = 1 if cost == 2 else 2
                        heapq.heappush(min_heap, (new_time, nr, nc, new_cost))
        

        return -1
