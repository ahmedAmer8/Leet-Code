class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        first = second = 0
        result = []
        size = len(s)
        while first < size:
            if s[first] == c: break
            first += 1
        for i in range(size):
            while second < size:
                if s[second] == c and second != first:break
                second += 1
            if i == second:
                first = second
            if second < size:
                m = min(abs(first - i), abs(second - i))
            else:
                m = abs(first-i)
            result.append(m)
        return result
