class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        adj = defaultdict(list)
        in_degree = [0]*numCourses
        for to, fr in prerequisites:
            adj[fr].append(to)
            in_degree[to] += 1
        print(adj)
        heap = []
        for node, count in enumerate(in_degree):
            heappush(heap, (count, node))
        # the old version stops when adj is empty, this means it stops
        # when the remaining courses have no prerequisites
        # it does not stop when we proccess all courses
        while len(res) < numCourses:
            deg, node = heappop(heap)
            res.append(node)
            if deg != 0:
                return []
            for nei in adj[node]:
                in_degree[nei] -= 1
                heappush(heap, (in_degree[nei], nei))
            adj.pop(node)
            
        return res
