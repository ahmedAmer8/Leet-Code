class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        max_heap = [-n for n in nums]
        heapify(max_heap)
        score = 0
        for i in range(k):
            cur = heappop(max_heap)
            score -= cur
            heappush(max_heap, floor(cur/3)) # for handling negative values
        return score
