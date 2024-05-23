class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'I': 1,
                    'V': 5,
                    'X': 10,
                    'L': 50,
                    'C': 100,
                    'D': 500,
                    'M': 1000}
        result = 0
        i = 0
        while i < len(s) -1:
            if values[s[i]] >= values[s[i+1]]:
                result += values[s[i]]
                i += 1
            else:
                result += values[s[i+1]] - values[s[i]]
                i += 2
        result += values[s[-1]] if i == len(s) - 1 else 0
        return result
