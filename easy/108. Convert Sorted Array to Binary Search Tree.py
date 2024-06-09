# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def balanced_tree(start, end):
            if start > end:
                return
            mid = (start+end)//2
            root = TreeNode(nums[mid])
            root.left = balanced_tree(start, mid-1)
            root.right = balanced_tree(mid+1, end)
            return root
        return balanced_tree(0, len(nums)-1)
