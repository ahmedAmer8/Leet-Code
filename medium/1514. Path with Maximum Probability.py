class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = defaultdict(list)
        for i in range(len(edges)):
            s, e, p = edges[i][0], edges[i][1], succProb[i]
            adj[s].append((e, p))
            adj[e].append((s, p))
        
        probs = [0.0] * n
        probs[start] = 1

        max_heap = [(-1, start)]
        while max_heap:
            p1, n1 = heapq.heappop(max_heap)
            p1 *= -1
            if n1 == end:
                return p1
            if p1 < probs[n1]:
                continue
            for n, p in adj[n1]:
                if p1*p > probs[n]:
                    probs[n] = p1*p
                    heapq.heappush(max_heap, (-probs[n], n))

        return 0.0
