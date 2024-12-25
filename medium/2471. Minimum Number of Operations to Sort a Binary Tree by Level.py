# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        count = 0
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            sortedLevel = list(sorted(level))
            numToIndex = {k:v for (v, k) in enumerate(level)}
            for i in range(len(level)):
                pivot = sortedLevel[i]
                if level[i] != pivot: 
                    count += 1
                    j = numToIndex[pivot]
                    numToIndex[pivot] = i
                    numToIndex[level[i]] = j
                    level[j] = level[i]
                    level[i] = pivot    
        return count
