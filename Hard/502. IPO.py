class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pairs = sorted(zip(profits, capital), key=lambda i:i[1])
        it = 0
        n = len(pairs)
        heap = []
        for i in range(k):
            while it < n and pairs[it][1] <= w:
                heapq.heappush(heap, -pairs[it][0])
                it += 1
            if heap: w -= heapq.heappop(heap)
        return w
