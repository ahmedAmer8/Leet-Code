class Solution:
    def findScore(self, nums: List[int]) -> int:
        marked = set()
        length = len(nums)
        heap = [(n, i) for i, n in enumerate(nums)]
        heapq.heapify(heap)
        score = 0
        while len(marked) < length:
            while heap:
                n, i = heapq.heappop(heap)
                if i in marked:
                    continue
                marked.add(i)
                if i > 0:
                    marked.add(i-1)
                if i < length -1:
                    marked.add(i+1)
                score += n
        return score
