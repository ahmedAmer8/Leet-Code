class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        res = []
        heap = [(-ord(ch), v) for ch,v in Counter(s).items()]
        heapify(heap)

        while heap:
            k, v = heappop(heap)
            if res and res[-1] == k:
                if not heap: break
                k2, v2 = heappop(heap)
                res.append(k2)
                if v2 -1 > 0:
                    heappush(heap, (k2, v2-1))
                heappush(heap, (k, v))
            else:
                reps = min(v, repeatLimit)
                res.extend([k]*reps)
                v -= reps
                if v > 0:
                    heappush(heap, (k, v))
                
        return ''.join(chr(-ch) for ch in res)
