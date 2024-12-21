# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def construct(arr, l, r):
    if l == r:
        return None
    idx = findMax(arr, l, r)
    root = TreeNode(arr[idx])
    root.left = construct(arr, l, idx)
    root.right = construct(arr, idx+1, r)
    return root

def findMax(arr, l, r):
    idx = l
    for i in range(l, r):
        if arr[i] > arr[idx]:
            idx = i
    return idx
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return construct(nums, 0, len(nums))

