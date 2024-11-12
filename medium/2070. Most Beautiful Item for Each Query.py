class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key= lambda x: (x[0], x[1]))
        n = len(items)
        max_beauty = 0
        for i in range(n):
            max_beauty = max(max_beauty, items[i][1])
            items[i][1] = max_beauty
        def binarySearch(p):
            l, r = 0, n-1
            ans = 0
            while l <= r:
                m = l + (r-l) // 2
                if items[m][0] <= p:
                    ans = items[m][1]
                    l = m + 1
                else:
                    r = m - 1
            return ans
        return [binarySearch(p) for p in queries]
