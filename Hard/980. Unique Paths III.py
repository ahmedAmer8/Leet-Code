class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # find starting, ending, count
        m, n = len(grid), len(grid[0])
        start = None
        cellsCount = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 0:
                    cellsCount += 1

        self.res = 0
        def solve(i, j, count):
            if not (0 <= i < m and 0 <= j < n and grid[i][j] >= 0):
                return
            if grid[i][j] == 2:
                self.res += count == cellsCount
                return
            grid[i][j] = -2
            solve(i, j+1, count+1)
            solve(i+1, j, count+1)
            solve(i, j-1, count+1)
            solve(i-1, j, count+1)
            grid[i][j] = 0
            
        solve(start[0], start[1], -1)
        return self.res
        
