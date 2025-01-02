class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(words)
        prefix = [0]*(n+1)
        for i in range(n):
            w = words[i]
            if w[0] in vowels and w[-1] in vowels:
                prefix[i+1] = prefix[i] + 1
            else:
                prefix[i+1] = prefix[i]
        res = []
        for s, en in queries:
            if s == 0:
                res.append(prefix[en+1])
                continue
            res.append(prefix[en+1] - prefix[s])
        return res
