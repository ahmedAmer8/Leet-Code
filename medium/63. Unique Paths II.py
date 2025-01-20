class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = {}
        def solve(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i >= m or j >= n or grid[i][j] == 1:
                memo[(i, j)] = 0
                return 0
            if i == m-1 and j == n-1:
                memo[(i, j)] = 1
                return 1
            memo[(i, j)] = solve(i+1, j) + solve(i, j+1)
            return memo[(i, j)]
        return solve(0, 0)
