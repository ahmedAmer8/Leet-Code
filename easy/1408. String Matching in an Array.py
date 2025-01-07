class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        substrings = defaultdict(int)
        for w in words:
            subs = [w[i:j] for i in range(len(w)) for j in range(i+1, len(w)+1)]
            for s in subs:
                substrings[s] += 1

        res = []
        for w in words:
            if substrings.get(w, 0) > 1:
                res.append(w)
            
        return res
        
