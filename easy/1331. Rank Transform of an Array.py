class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return
        sorted_arr = sorted(arr)
        n = len(sorted_arr)
        ranks = {sorted_arr[0]:1}
        rank = 1
        for i in range(1, n):
            if sorted_arr[i] != sorted_arr[i-1]:
                rank += 1
            ranks[sorted_arr[i]] = rank
        return [ranks[i] for i in arr]
