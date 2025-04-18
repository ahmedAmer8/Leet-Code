class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows, cols = defaultdict(int), defaultdict(int)
        n = len(grid)
        for i in range(n):
            row, col = "", ""
            for j in range(n):
                row += str(grid[i][j]) + '.'
                col += str(grid[j][i]) + '.'

            rows[row] += 1
            cols[col] += 1

        res = 0
        for row, freq in rows.items():
            res += freq * cols[row]
        
        return res
