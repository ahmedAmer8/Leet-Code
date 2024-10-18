class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = []
        def maxlocal(i, j):
            mx = 0
            for k in range(i, i+3):
                for l in range(j, j+3):
                    mx = max(mx, grid[k][l])
            return mx
        for i in range(n-2):
            temp = []
            for j in range(n-2):
                temp.append(maxlocal(i, j))
            res.append(temp.copy())

        return res
