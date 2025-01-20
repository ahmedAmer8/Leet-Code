class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        numToPosition = {}
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                numToPosition[mat[i][j]] = (i, j)
                
        rowSize = {r: n for r in range(m)}
        colSize = {c: m for c in range(n)}

        for i, n in enumerate(arr):
            r, c = numToPosition[n]
            rowSize[r] -= 1
            colSize[c] -= 1
            if rowSize[r] == 0 or colSize[c] == 0:
                return i
        
        
