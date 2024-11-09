# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fast = head
        for i in range(1, k):
            fast = fast.next

        first = fast
        second = head
        while fast.next:
            fast = fast.next
            second = second.next
        first.val, second.val, = second.val, first.val
        return head

