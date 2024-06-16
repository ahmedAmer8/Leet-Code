class Solution:
    def largestInteger(self, num: int) -> int:
        num = [int(i) for i in str(num)]
        odd_nums = [-i for i in num if i % 2 == 1]
        even_nums = [-i for i in num if i % 2 == 0]
        heapq.heapify(odd_nums)
        heapq.heapify(even_nums)
        res = ''
        for i in num:
            if i % 2 == 0:
                res += str(-heapq.heappop(even_nums))
            else:
                res += str(-heapq.heappop(odd_nums))
        return int(res)
        
