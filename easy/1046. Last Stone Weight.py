class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heap = heapq.heapify(stones)
        while len(stones) > 1:
            mx1, mx2 = -heapq.heappop(stones), -heapq.heappop(stones)
            heapq.heappush(stones, mx2-mx1)
        return -stones[0]
