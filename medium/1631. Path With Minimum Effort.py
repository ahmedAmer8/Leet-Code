class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])

        efforts = [[float('inf')] * cols for _ in range(rows)]
        efforts[0][0] = 0
        heap = [(0, 0, 0)]

        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        
        def valid(row, col):
            return 0 <= row < rows and 0 <= col < cols
        
        while heap:
            effort, x, y = heappop(heap)
            if (x, y) == (rows-1, cols-1):
                return effort

            for dr, dc in directions:
                x2, y2 = x+dr, y+dc
                if valid(x2, y2):
                    cur_effort = max(effort, abs(heights[x][y] - heights[x2][y2]))
                    if cur_effort < efforts[x2][y2]:
                        efforts[x2][y2] = cur_effort
                        heappush(heap, (cur_effort, x2, y2))
        

                
