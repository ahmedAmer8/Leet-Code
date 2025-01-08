class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res = 0
        n = len(words)
        for i in range(n):
            str1 = words[i]
            for j in range(i+1, n):
                str2 = words[j]
                l1 = len(str1)
                l2 = len(str2)
                if l2 < l1:
                    continue
                if str2[:l1] == str1 and str2[l2-l1:] == str1:
                    res += 1
        return res
