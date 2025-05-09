class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
            
        n = len(grid)
        distance = [[float('inf')] * n for _ in range(n)]
        distance[0][0] = 1

        min_heap = [(1, 0, 0)]

        while min_heap:
            dist, r, c = heapq.heappop(min_heap)
            
            if (r, c) == (n-1, n-1):
                return dist
            
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, 1), (1, -1)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    if dist + 1 < distance[nr][nc]:
                        distance[nr][nc] = dist + 1
                        heapq.heappush(min_heap, (dist+1, nr, nc))


        return -1
