class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freq = Counter(digits)
        res = []

        for n in range(100, 1000, 2):
            x, y, z = n%10, (n//10)%10, n // 100
            temp = Counter([x, y, z])
            if temp[x] <= freq[x] and temp[y] <= freq[y] and temp[z] <= freq[z]:
                res.append(n)
        
        return res
