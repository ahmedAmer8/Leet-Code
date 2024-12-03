class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        cur = 0
        stringArray = []
        for idx in spaces:
            stringArray.extend(s[cur:idx])
            cur = idx
            stringArray.append(' ')
        stringArray.extend(s[cur:]) 
        return ''.join(stringArray)
