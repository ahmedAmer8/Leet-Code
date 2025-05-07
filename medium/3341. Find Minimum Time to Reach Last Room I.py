class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        # shortest path
        n, m = len(moveTime), len(moveTime[0])
        

        min_heap = [(0, 0, 0)]
        arrival_time = [[float('inf')] * m for _ in range(n)]
        arrival_time[0][0] = 0

        while min_heap:
            t, r, c = heapq.heappop(min_heap)
            if (r, c) == (n-1, m-1):
                return t
            
            if t > arrival_time[r][c]:
                continue
            
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < n and 0 <= nc < m:
                    nt = max(t, moveTime[nr][nc]) + 1
                    
                    if nt < arrival_time[nr][nc]:
                        heapq.heappush(min_heap, (nt, nr, nc))
                        arrival_time[nr][nc] = nt
            
        return -1

