class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # for each prefix, check if it seen before or not
        res = set()
        folder.sort()
        for f in folder:
            found = False
            for i in range(len(f)):
                if f[i] == '/':
                    cur = f[:i]
                    if cur in res:
                        found = True
                        break
            if not found:
                res.add(f)
        return list(res)
