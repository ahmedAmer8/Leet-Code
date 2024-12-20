# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        l = 0
        while q:
            if l & 1:
                reverse = list(reversed([n.val for n in q]))
                i = 0
                for n in q:
                    n.val = reverse[i]
                    i += 1


            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            l += 1
        return root


            

