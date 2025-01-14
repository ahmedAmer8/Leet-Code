class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        res = [0]*n
        freq = [0]*(n+1)
        curCount = 0
        for i in range(n-1):
            freq[A[i]] += 1
            curCount += 1 if freq[A[i]] == 2 else 0
            freq[B[i]] += 1
            curCount += 1 if freq[B[i]] == 2 else 0
            res[i] = curCount
        res[n-1] = n
        return res
        
