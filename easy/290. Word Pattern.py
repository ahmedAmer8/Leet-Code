class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hashmap = {}
        reverse = {}
        words = s.split()
        if len(pattern) != len(words):
            return False
        for i in range(len(pattern)):
            if pattern[i] in hashmap and hashmap[pattern[i]] != words[i] or words[i] in reverse and reverse[words[i]] != pattern[i]:
                return False
            hashmap[pattern[i]] = words[i]
            reverse[words[i]] = pattern[i]
        return True
