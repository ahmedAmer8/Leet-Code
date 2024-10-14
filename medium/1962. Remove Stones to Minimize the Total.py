class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        res = sum(piles)
        max_heap = [-n for n in piles]
        heapify(max_heap)    # heapify is O(n) time

        for i in range(k):
            cur = -heappop(max_heap)
            op = floor(cur/2)
            res -= op
            heappush(max_heap, -cur + op)
        return res
