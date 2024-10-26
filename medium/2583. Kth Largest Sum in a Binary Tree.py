# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        max_heap = []
        q = deque()
        q.append(root)
        while q:
            res = 0
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                res += node.val
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            heappush(max_heap, -res)
        if len(max_heap) < k:
            return -1
        for i in range(k-1):
            heappop(max_heap)
        return -heappop(max_heap)
            
