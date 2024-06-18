class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        h = defaultdict(list)
        res = []
        for i in range(len(groupSizes)):
            h[groupSizes[i]].append(i)
            if len(h[groupSizes[i]]) == groupSizes[i]:
                res.append(h[groupSizes[i]])
                h.pop(groupSizes[i])
        return res
