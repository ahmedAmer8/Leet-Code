# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        dq = deque()
        dq.append((root, root))
        x_data = [-1, -1]
        y_data = [-1, -1]
        depth = 0
        while len(dq) > 0:
            for i in range(len(dq)):
                node, parent = dq.popleft()
                if node.val == x:
                    x_data = [parent.val, depth]
                if node.val == y:
                    y_data = [parent.val, depth]
                if node.left:
                    dq.append((node.left, node))
                if node.right:
                    dq.append((node.right, node))
            depth += 1
        print(x_data)
        print(y_data)
        return x_data[0] != y_data[0] and x_data[1] == y_data[1]
        
