class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        res = []
        supplies = set(supplies)
        adj = defaultdict(list)
        in_degree = [0] * len(recipes)
        recipe_idx = {r:i for i, r in enumerate(recipes)}

        for i, r in enumerate(recipes):
            for ing in ingredients[i]:
                if ing not in supplies:
                    if ing in recipe_idx:
                        adj[recipe_idx[ing]].append(i)
                    in_degree[i] += 1

        heap = []
        for r, count in enumerate(in_degree):
            heapq.heappush(heap, (count, r))


        while len(res) < len(recipes):
            deg, r = heapq.heappop(heap)
            if deg > 0:
                return res
            for nei in adj[r]:
                in_degree[nei] -= 1
                heapq.heappush(heap, (in_degree[nei], nei))
            supplies.add(recipes[r])
            adj.pop(r)
            res.append(recipes[r])
            
        return res
