class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        in_degree = [0]*numCourses
        for to, fr in prerequisites:
            adj[fr].append(to)
            in_degree[to] += 1
        heap = []
        for node, count in enumerate(in_degree):
            heappush(heap, (count, node))

        while len(adj) > 0:
            deg, node = heappop(heap)
            if deg != 0:
                return False
            for nei in adj[node]:
                in_degree[nei] -= 1
                heappush(heap, (in_degree[nei], nei))
            adj.pop(node)
            
        
        return True
