class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-i for i in gifts]
        heapq.heapify(gifts)
        while gifts and k > 0:
            x = -heapq.heappop(gifts)
            x = math.floor(math.sqrt(x))
            heapq.heappush(gifts, -x)
            k -= 1
        return -sum(gifts)
