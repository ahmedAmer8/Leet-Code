# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dq = deque()
        dq.append(root)
        level_sum = []
        while len(dq) > 0:
            cur_sum = 0
            for i in range(len(dq)):
                node = dq.popleft()
                cur_sum += node.val
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            level_sum.append(cur_sum)

        dq.append(root)
        root.val = 0
        level = 1
        while len(dq) > 0:
            for i in range(len(dq)):
                node = dq.popleft()
                left = right = 0
                if node.left:
                    left = node.left.val
                if node.right:
                    right = node.right.val
                if node.left:
                    node.left.val = level_sum[level] - (right+left)
                    dq.append(node.left)
                    
                if node.right:
                    node.right.val = level_sum[level] - (right+left)
                    dq.append(node.right)
                    
            level += 1

        return root
