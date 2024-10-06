class Solution:
    def areSentencesSimilar(self, sen1: str, sen2: str) -> bool:

        sen1, sen2 = list(sen1.split()), list(sen2.split())
        s1 = s2 = 0
        e1, e2 = len(sen1)-1, len(sen2)-1
        while s1 <= e1 and s2 <= e2:
            if sen1[s1] == sen2[s2]:
                s1 += 1
                s2 += 1
            elif sen1[e1] == sen2[e2]:
                e1 -= 1
                e2 -= 1
            else:
                return False
        return True
        
