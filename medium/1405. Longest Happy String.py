class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        heap = []
        for count, ch in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if count != 0:
                heappush(heap, (count, ch))
        while heap:
            count, ch = heappop(heap)
            if len(res) > 1 and res[-1] == res[-2] == ch:
                if not heap:
                    break
                count2, ch2 = heappop(heap)
                res += ch2
                count2 += 1
                if count2:
                    heappush(heap, (count2, ch2))
            else:
                res += ch
                count += 1
            if count:
                heappush(heap, (count, ch))
            
        return res
