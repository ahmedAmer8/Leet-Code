# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        v = []
        def dfs(r):
            if not r:
                return
            dfs(r.left)
            v.append(r)
            dfs(r.right)
        dfs(root)

        def bst(v):
            if not v:
                return None
            m = len(v)//2
            root = v[m]
            root.left = bst(v[:m])
            root.right = bst(v[m+1:])
            return root
        return bst(v)
        
