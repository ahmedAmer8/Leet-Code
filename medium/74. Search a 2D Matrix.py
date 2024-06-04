class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ans = -1
        l, r = 0, len(matrix)-1
        while l <= r:
            m = l + (r-l)//2
            if matrix[m][0] <= target:
                ans = m
                l = m + 1
            else:
                r = m - 1
        if ans != -1:
            l, r = 0, len(matrix[ans])-1
            while l <= r:
                m = l + (r-l)//2
                if matrix[ans][m] == target:
                    return True
                elif matrix[ans][m] > target:
                    r = m -1
                else:
                    l = m + 1
        return False
